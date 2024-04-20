from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import CustomUserCreationForm,UserLoginForm
from django.shortcuts import render, redirect

from .models import CustomUser

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.type = "visitor"
            user.save()
            login(request, user)
            return redirect('base:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})




def login_view(request):
    print(request)
    
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user_exist = authenticate(request,username=form.cleaned_data["username"],password=form.cleaned_data["password"])
            print(user_exist)
            if user_exist is not None:
                user = CustomUser.objects.get(username=form.cleaned_data["username"])
                login(request, user)
                return redirect('base:index')
            
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


