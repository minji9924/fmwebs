# Create your views here.
from django.contrib.auth import authenticate, login
from common.forms import UserForm
from django.shortcuts import render, redirect


def signup(request):
    if request.method == "POST":  # POST 요청인 경우에는 화면에서 입력한 데이터로 사용자를 생성
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')  # form.cleaned_data.get을 사용해서 폼의 입력값을 개별적으로 얻음
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증 - username과 password가 정확한지 검증
            login(request, user)  # 로그인 - user session 담당
            return redirect('index')
    else:
        form = UserForm()  # GET 요청이면 회원가입 화면을 보여줌
    return render(request, 'common/signup.html', {'form': form})