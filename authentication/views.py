from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from online_enrollment.models import Profile

# ----------------------------
# REGISTER VIEW
# ----------------------------
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('authentication:login')
    else:
        form = UserRegisterForm()
    
    return render(request, 'authentication/register.html', {'form': form})



# ----------------------------
# LOGIN VIEW
# ----------------------------
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('online_enrollment:home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'authentication/login.html')


# ----------------------------
# LOGOUT VIEW
# ----------------------------
@login_required(login_url='authentication:login')
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('authentication:login')
