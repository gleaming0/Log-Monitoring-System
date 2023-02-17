from django.shortcuts import render, redirect
from common.forms import UserForm
from django.contrib.auth import authenticate, login


# Create your views here.

def signup(request):
    if request.method == "POST":
        print("로그인 시도")
        form = UserForm(request.POST)
        if form.is_valid():
            print("값 검증")
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()

    return render(request, 'common/signup.html', {'form': form})
