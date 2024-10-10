from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Customers

def home(request):
    customers = Customers.objects.all()

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
        return render(request, 'home.html', {'customers':customers})

def logout_user(request):
    logout(request)
    messages.warning(request, "You Have Been Logged Out...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        # if form is valid, save
        if form.is_valid():
            form.save()

            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user = authenticate(username=username, password=password)

            login(request, user)
            messages.success(request, "Register Successfully")

            return redirect('home')
        
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    
    return render(request, 'register.html', {'form': form})
            
def customer(request, pk):
    if request.user.is_authenticated:
        customer = Customers.objects.get(id=pk)
        return render(request, 'customer.html', {'customer': customer})
    else:
        messages.error(request, "You must be logged in to view that page")
        return redirect('home')
    
def delete_customer(request, pk):
    if request.user.is_authenticated:
        customer = Customers.objects.get(id=pk)
        customer.delete()
        messages.error(request, "Reacord delete successfully")
        return redirect('home')
    else:
        messages.error(request, "You must be logged in to view that page")
        return redirect('home')