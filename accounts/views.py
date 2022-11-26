from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import  UserRegistrationForm #,CustomUserCreationForm,
from .forms import LoginForm
from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.


# class LoginForm(TemplateView):
#     template_name = "accounts/loginForm.html"


# class RegisterForm(TemplateView):
#     template_name = "accounts/registerForm.html"


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
                    return redirect('homepage')
                else:
                    messages.error(request, "The login failed!")
                    # return HttpResponse('Invalid login')
                    return redirect('login')
            else:
                messages.error(request, "The login failed!")
                # return HttpResponse('Invalid login')
                return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'accounts/loginForm.html', {'form': form})

# def signup(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request,'accounts/registerForm.html',{'form':form})

# def signup(request):  
#     if request.POST == 'POST':  
#         form = CustomUserCreationForm()  
#         if form.is_valid():  
#             form.save()  
#     else:  
#         form = CustomUserCreationForm()  
#         context = {  
#         'form':form  
#     }  
#     return render(request, 'accounts/registerForm.html', context) 
def signup(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # return render(request,
            #             'accounts/loginForm.html',
            #             {'new_user': new_user})
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
    return render(request,
                        'accounts/registerForm.html',
                        {'user_form': user_form})