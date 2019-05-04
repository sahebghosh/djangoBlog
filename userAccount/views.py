from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

def home(request):
    return render(request, 'userAccount/home.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulation, you have been Successfully registered.....')
            #user = form.save()
            #login(request, user)
            return redirect('userAccount:login')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'userAccount/signup.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('blog:list')
    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'userAccount/login.html', context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Successfully, you have been logged out.....')
        return redirect('userAccount:login')
