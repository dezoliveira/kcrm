from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # Check if user is logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.error(request, "Error - Invalid credentials")
            return redirect('home')
        
    else:
        return render(request, 'home.html', {})

def login_user(request):
    pass

def logout_user(request):
    pass