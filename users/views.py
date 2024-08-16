from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def dashboard(request):
    if request.user.user_type == 'patient':
        return render(request, 'patient_dashboard.html', {'user': request.user})
    elif request.user.user_type == 'doctor':
        return render(request, 'doctor_dashboard.html', {'user': request.user})
