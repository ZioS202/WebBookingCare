from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import  UserRegistrationForm #,CustomUserCreationForm,
from .forms import SigninForm, UpdateProfileForm, UpdateUserForm
from django.shortcuts import redirect, render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


# class LoginForm(TemplateView):
#     template_name = "accounts/loginForm.html"


# class RegisterForm(TemplateView):
#     template_name = "accounts/registerForm.html"

def user_signout(request):
    logout(request)
    return render(request, 'accounts/signoutForm.html')
      
def user_signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
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
            else:
                messages.error(request, "Your account is not exist! Please create a new account!")
    else:
        form = SigninForm()
    return render(request, 'accounts/signinForm.html', {'form': form})

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
            messages.info(request, "You created a new account!")
            return redirect('signin')
        else:
            messages.error(request, "Can not create your account! May be username is used or 2 passwords are not the same! Please try again!")
    else:
        user_form = UserRegistrationForm()
    return render(request, 'accounts/signupForm.html', {'user_form': user_form})

def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.info(request, 'Cập nhật thông tin cá nhân thành công!')
            return redirect('profile')
        else:
            messages.error(request, 'Cập nhật thông tin cá nhân thất bại!')
            user_form = UpdateUserForm(instance=request.user)
            profile_form = UpdateProfileForm(instance=request.user)
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user)
        messages.info(request, 'Đây là không gian lưu trữ tài khoản "Booking Care" của bạn!')

    return render(request, 'accounts/profileUser.html', {'user_form': user_form, 'profile_form': profile_form})