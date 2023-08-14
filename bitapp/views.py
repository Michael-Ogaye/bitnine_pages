
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import render, redirect

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in.
            auth_login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'bitapp/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')  # Redirect to the appropriate URL after login
            else:
                # Invalid credentials
                form.add_error(None, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'bitapp/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

def home_view(request):
    return render(request,'bitapp/home.html')


