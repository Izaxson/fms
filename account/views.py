from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from django.views import View

class LoginView(View):
    def get(self, request):
        return render(request, 'fms/auth/login.html')

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('dashboard')
        else:
            # Return an 'invalid login' error message.
            messages.error(request, "An error occurred.")
            return redirect('login')
        
class LogoutView(View):
    def get(self, request):
        logout(request)
        # Redirect to a success page.
        return redirect('login')

       