from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from common.forms import UserForm

def login_view(request):
    return render(request, 'common/login.html')

def index(request):
    return render(request, 'common/index.html')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('polls:index')  # 회원가입 후 polls 앱의 index 페이지로 리다이렉트
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})    

def logout_view(request):
    logout(request)
    return redirect('polls:index')  

