from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignupForm

def home(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request," You Have Been Logged in!!")
            return redirect('home')
        else:
            messages.success(request,"There was an error. Please Try again")
            return redirect('home')
    else:
        return render(request,'home.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,"You Have Been Logged Out...!")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You Have Successfully Registered..!!")
                return redirect('home')
    else:
        form = SignupForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})