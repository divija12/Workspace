from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
        if request.method =="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')

            User=authenticate(request, username=username, password=password)
            print(username)
            if User is not None:
                login(request, User)
                return redirect('employdata')
            else:
                messages.info(request, 'Username or Password is incorrect')

        return render(request, 'employee/loginpage.html')

@login_required
def employdata(request):
    return render(request, 'employee/employdata.html')
def logoutUser(request):
    logout(request)
    return redirect('home')