from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
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
# def logout_request(request):
#     logout(request)
#     return redirect('logout')

class LogoutForm(TemplateView):
      template_name = "accounts/logoutForm.html"
      
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
                    messages.error(request, "The account is disabled!")
                    # return HttpResponse('Invalid login')
                    #return redirect('login')
            else:
                messages.error(request, "Your account is not exist! Please create a new account!")
                # return HttpResponse('Invalid login')
                #return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'accounts/loginForm.html', {'form': form})

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
            messages.error(request, "Can not create your account! May be username is used or 2 passwords are not the same! Please try again!")
    else:
        user_form = UserRegistrationForm()
    return render(request, 'accounts/registerForm.html', {'user_form': user_form})