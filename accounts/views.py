from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import  UserRegistrationForm
from .forms import SigninForm, UpdateProfileForm, UpdateUserForm
from django.shortcuts import redirect, render
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.

@login_required(login_url='/accounts/signin')
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
            subject = 'Welcom to "Booking Care"!'
            message = f'Hi {new_user.username}, thank you for registering in "Booking Care". Good a happy day!'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [new_user.email, ]
            send_mail( subject, message, email_from, recipient_list )
            return redirect('signin')
        else:
            messages.error(request, "Can not create your account! May be username is used or 2 passwords are not the same! Please try again!")
    else:
        user_form = UserRegistrationForm()
    return render(request, 'accounts/signupForm.html', {'user_form': user_form})

@login_required(login_url='/accounts/signin')
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