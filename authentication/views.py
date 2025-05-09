from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from .forms import *
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form_intance = form.save(commit=False)
            form_intance.mobile_number = request.POST['mobile_number']
            form_intance.bio = request.POST['bio']
            form_intance.profile_pic = request.FILES['profile_pic']
            form_intance.cover_pic = request.FILES['cover_pic']
            form_intance.save()
            messages.success(request,'Registration success')
            return redirect('/auth/login')
            
    else:
        form = RegistrationForm()

    context = {'form':form}
    return render(request,'authentication/register.html',context)

def handlelogin(request):
    if request.method == 'POST':
        form = LoginForm(request, data= request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                
                login(request,user)
                messages.success(request,'Login successful')
                print('hello')
                return redirect('social:home')
            else:
                print('hello')
                messages.error(request,'Invalid username or passdword')

            

    else:
        form = LoginForm()
    context = {'form':form}
    return render(request,'authentication/login.html',context)

def handlelogout(request):
    logout(request)
    messages.success(request,'Logout succuessfully')
    
    return redirect('/auth/login')