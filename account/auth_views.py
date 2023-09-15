from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from .forms import LoginForm
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
        user = authenticate(request,
        username=cd['username'],
        password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request,'Login Success')
                return render (request,'fms/dashboard.html')
            else:
                return HttpResponse('Disabled account')
        else:
            messages.error(request,'Login Success')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')