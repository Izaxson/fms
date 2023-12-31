import math
import os
from sqlite3 import DatabaseError
from django.http import FileResponse, Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
import os
from django.conf import settings
from django.views.generic import CreateView,ListView,DetailView,FormView,UpdateView,DeleteView
from django.contrib import messages
from django.contrib.auth.models import User
from core import settings
from fms.filter import ReceivedFilter, SentFilter
from fms.forms import ReceivedForm, SentForm,UpdateReceivedForm,UpdateSentForm
import mimetypes
from django.views.generic import TemplateView
from .models import Received, Sent  # Import the Received and Sent models
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q






class DashboardView(TemplateView):
    template_name = 'fms/dashboard.html'
    login_url = '/account/login/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        try:
            received_count = Received.objects.all().count()
            sent_count = Sent.objects.all().count()
            users_count = User.objects.all().count()
            # Calculate the total count
            total_count = received_count + sent_count
            percent_received=(math.floor( (received_count/total_count)*100))
            percent_sent=(math.floor( (sent_count/total_count)*100))
            context['received_count'] = received_count
            context['users_count'] = users_count
            context['sent_count'] = sent_count
            context['total_count'] = total_count  # Add the total count to the context
            context['percent_received'] = percent_received
            context['percent_sent'] = percent_sent
        except Exception as e:
            # Handle any exceptions gracefully
            context['received_count'] = "loading...."
            context['sent_count'] = "loading...."
            context['total_count'] = "loading...."
            context['users_count'] = "loading...."
        
        return context

 


class ReceivedListView(FilterView):
    template_name = 'fms/incoming/received.html'
    model = Received
    context_object_name = 'received'
    filterset_class = ReceivedFilter
    # paginate_by = 35 # display  items per page

    # def get_queryset(self):
    #     # Return a queryset of all Expense objects of current logged in user
    #      return Received.objects.all() 
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # queryset = queryset.filter(profile=self.request.user.profile)

        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(name=search_query) ,
                Q(subject__icontains=search_query)
            )

        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs
    #search Received

class SearchReceivedListView(FilterView):
    template_name = 'fms/incoming/search.html'
    model = Received
    context_object_name = 'search'
    filterset_class = ReceivedFilter
    # paginate_by = 35 # display  items per page

    # def get_queryset(self):
    #     # Return a queryset of all Expense objects of current logged in user
    #      return Received.objects.all() 
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # queryset = queryset.filter(profile=self.request.user.profile)

        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(name=search_query) ,
                Q(subject__icontains=search_query)
            )

        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs
        
# class ReceivedAddView(FormView):
#     template_name = 'fms/incoming/addreceived.html'
#     form_class=ReceivedForm
#     success_url = reverse_lazy('received')

#     def form_valid(self, form):
#         # profile = self.request.user.profile  #  'Profile' model related to the user
#         # received = form.save(commit=False)
#         # received.profile = profile
#         form.save()
#         #handling form error
#     def form_invalid(self, form):
#         messages.error(self.request, 'There was an error in your form. Please correct the errors below.')
#         return self.render_to_response(self.get_context_data(form=form))
#         messages.success(self.request, 'Your File has been saved. Thank you!')
#         return super().form_valid(form)
    
class ReceivedAddView(FormView):
    template_name = 'fms/incoming/addreceived.html'
    form_class = ReceivedForm
    success_url = reverse_lazy('addreceived')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your File has been saved. Thank you!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'There was an error in your form. Please correct the errors below.')
        return self.render_to_response(self.get_context_data(form=form))


class UpdateReceived(UpdateView):
    template_name = 'fms/incoming/editreceived.html'
    form_class = UpdateReceivedForm
    success_url = reverse_lazy('received')

    def form_valid(self, form):
        form.save()

        messages.success(self.request, 'Your File details has been updated. Thank you!')
        return super().form_valid(form)

    def get_object(self, queryset=None):
        file_id = self.kwargs.get('file_id')
        return Received.objects.get(pk=file_id) 

class DeleteReceived(DeleteView):
    model = Received
    success_url = reverse_lazy('received')  # Redirect to the success URL after deletion

    def get_object(self, queryset=None):
        file_id = self.kwargs.get('file_id')
        return get_object_or_404(Received, id=file_id)


 
class SentListView(FilterView):
    template_name = 'fms/outgoing/sent.html'
    model = Sent
    context_object_name = 'sent'
    filterset_class = SentFilter
 
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # queryset = queryset.filter(profile=self.request.user.profile)

        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(name=search_query) ,
                Q(Vehicle__icontains=search_query)
            )

        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs
class SearchSentListView(FilterView):
    template_name = 'fms/outgoing/search.html'
    model = Sent
    context_object_name = 'search'
    filterset_class = SentFilter
  
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # queryset = queryset.filter(profile=self.request.user.profile)

        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(name=search_query) ,
                Q(subject__icontains=search_query)
            )

        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs




class SentAddView(FormView):
    template_name = 'fms/outgoing/addsent.html'
    form_class=SentForm
    success_url = reverse_lazy('sent')

    def form_valid(self, form):
        # profile = self.request.user.profile  #  'Profile' model related to the user
        form.save()
        # form.profile = profile
        # form.save()

        messages.warning(self.request, 'Your File has been saved. Thank you!')
        return super().form_valid(form)   
    

class UpdateSent(UpdateView):
    template_name = 'fms/outgoing/editsent.html'
    form_class = UpdateSentForm
    success_url = reverse_lazy('sent')

    def form_valid(self, form):
        form.save()

        messages.success(self.request, 'Your File details has been updated. Thank you!')
        return super().form_valid(form)

    def get_object(self, queryset=None):
        file_id = self.kwargs.get('file_id')
        return Sent.objects.get(pk=file_id) 

class DeleteSent(DeleteView):
    model = Sent
    template_name = 'fms/outgoing/delete.html'
    success_url = reverse_lazy('sent')  # Redirect to the success URL after deletion

    def get_object(self, queryset=None):
        file_id = self.kwargs.get('file_id')
        return get_object_or_404(Sent, id=file_id)
    
class ReceivedDownloadFileView(View):
    def get(self, request, file_id):
        uploaded_file = Received.objects.get(pk=file_id)
        response = HttpResponse(
            uploaded_file.file, content_type='application/force-download'
        )
        response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
        return response
    
class SentDownloadFileView(View):
    def get(self, request, file_id):
        try:
            uploaded_file = Sent.objects.get(pk=file_id)
        except Sent.DoesNotExist:
            return HttpResponse("File not found", status=404)

        response = HttpResponse(
            uploaded_file.file.read(), content_type='application/force-download'
        )
        response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'

        return response


class SearchResultsView(FilterView):
    model = Received
    template_name = 'fms/incoming/search.html'  # Create this template
    filterset_class = ReceivedFilter
    context_object_name = 'search'
    paginate_by = 10  # Adjust as needed
    
    def get_queryset(self):
        form = ReceivedForm(self.request.GET)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            entity = form.cleaned_data.get('entity')
            institution = form.cleaned_data.get('institution')
            date_from = form.cleaned_data.get('date_from')
            date_to = form.cleaned_data.get('date_to')
            priority = form.cleaned_data.get('priority')
            
            queryset = Received.objects.all()
            
            # Apply filtering based on the form fields
            if subject:
                queryset = queryset.filter(subject__icontains=subject)
            if entity:
                queryset = queryset.filter(entity__icontains=entity)
            if institution:
                queryset = queryset.filter(institution__icontains=institution)
            if priority:
                queryset = queryset.filter(priority__icontains=priority)
            
            # Apply date range filtering if provided
            if date_from:
                queryset = queryset.filter(date_received__gte=date_from)
            if date_to:
                queryset = queryset.filter(date_received__lte=date_to)
            
            return queryset
        return Received.objects.none()
  
class ReceivedViewFile(View):
    def get(self, request, file_id):
        try:
            uploaded_file = Received.objects.get(pk=file_id)
        except Received.DoesNotExist:
            return HttpResponse("File not found", status=404)

        # Determine the content type based on the file extension
        file_name = uploaded_file.file.name
        content_type = 'application/octet-stream'  # Default content type for unknown files

        if file_name.endswith('.pdf'):
            content_type = 'application/pdf'
  
        response = HttpResponse(uploaded_file.file.read(), content_type=content_type)

        # Remove the 'Content-Disposition' header to prevent a download prompt
        del response['Content-Disposition']

        return response    
    

class SentViewFile(View):
    def get(self, request, file_id):
        try:
            uploaded_file = Sent.objects.get(pk=file_id)
        except Sent.DoesNotExist:
            return HttpResponse("File  not found", status=404)

        # Determine the content type based on the file extension
        file_name = uploaded_file.file.name
        content_type = 'application/octet-stream'  # Default content type for unknown files

        if file_name.endswith('.pdf'):
            content_type = 'application/pdf'
        
        response = HttpResponse(uploaded_file.file.read(), content_type=content_type)

        # Remove the 'Content-Disposition' header to prevent a download prompt
        del response['Content-Disposition']

        return response         