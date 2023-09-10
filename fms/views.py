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
from fms.forms import ReceivedForm, SentForm,UpdateReceivedForm,UpdateSentForm
from fms.models import Received, Sent
import mimetypes
from django.views.generic import TemplateView
from .models import Received, Sent  # Import the Received and Sent models

from django.contrib.auth.mixins import LoginRequiredMixin



class LoginView(TemplateView):
    template_name = 'fms/auth/login.html'
class PasswordResetView(TemplateView):
    template_name = 'fms/auth/password-reset.html'



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
            context['received_count'] = "no data."
            context['sent_count'] = "no data."
            context['total_count'] = "no data."
            context['users_count'] = "no data."
        
        return context

 


class ReceivedListView(ListView):
    template_name = 'fms/incoming/received.html'
    model = Received
    context_object_name = 'received'
    # paginate_by = 35 # display  items per page

    def get_queryset(self):
        # Return a queryset of all Expense objects of current logged in user
         return Received.objects.all() 
    
class ReceivedAddView(FormView):
    template_name = 'fms/incoming/addreceived.html'
    form_class=ReceivedForm
    success_url = reverse_lazy('received')

    def form_valid(self, form):
        # profile = self.request.user.profile  #  'Profile' model related to the user
        # received = form.save(commit=False)
        # received.profile = profile
        form.save()

        messages.success(self.request, 'Your File has been saved. Thank you!')
        return super().form_valid(form)
    

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


class SentListView(ListView):
    template_name = 'fms/outgoing/sent.html'
    model = Sent
    context_object_name = 'sent'
    # paginate_by = 10 # display 10 items per page

    def get_queryset(self):
        # Return a queryset of all Expense objects of current logged in user
         return Sent.objects.all()  


class SentAddView(FormView):
    template_name = 'fms/outgoing/addsent.html'
    form_class=SentForm
    success_url = reverse_lazy('sent')

    def form_valid(self, form):
        # profile = self.request.user.profile  #  'Profile' model related to the user
        form.save()
        # form.profile = profile
        # form.save()

        messages.success(self.request, 'Your File has been saved. Thank you!')
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



def pdf_view(request, filename):
    # Build the full file path to the PDF document
    filepath = os.path.join(settings.MEDIA_ROOT, "files", filename)

    try:
        with open(filepath, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline;filename=' + filename
            return response
    except FileNotFoundError:
        return render(request, '404.html')  # Handle file not found gracefully
from django.views.generic import ListView
from .models import Received
from .forms import ReceivedForm, UpdateReceivedForm, UpdateSentForm

class SearchResultsView(ListView):
    model = Received
    template_name = 'search_results.html'  # Create this template
    context_object_name = 'results'
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

class SentFileView(View):
    def get(self, request, sent_id):
        try:
            uploaded_file = Sent.objects.get(pk=sent_id)
        except Sent.DoesNotExist:
            return HttpResponse("File not found", status=404)

        response = HttpResponse(
            uploaded_file.sent.read(), content_type='application/force-download'
        )
        response['Content-Disposition'] = f'inline; filename="{uploaded_file.sent.name}"'
        return response