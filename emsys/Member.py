from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from baekjoon.models import CustomUser
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
#계급
class CustomUser(AbstractUser):
    RANK=[
        ('sprout','새싹'),
        ('user','엠시스 부원'),
        ('executive','엠시스 임원')
        ('admin','관리자')
    ]
    rank = models.CharField(max_length=10, choices=RANK, default='user')
    receive_event = models.BooleanField(default=False, verbose_name="이벤트 수신 동의")
    def __str__(self):
        return self.username
#회원가입
class Signup(UserCreationForm):
    eventagreeterms = forms.BooleanField(
        label="이벤트 수신에 동의합니다.",
        required=False
    )

    agreeterms = forms.BooleanField(
        label="이용약관에 동의합니다.",
        required=True,
        errormessages={'required': '이용약관에 동의해야 가입할 수 있습니다.'}
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
    def save(self, commit=True):
        user = super().save(commit=False)
        user.receive_event = self.cleaned_data.get('eventagreeterms', False)
        if commit:
            user.save()
        return user
#로그인
class Login(forms.Form):
    username=forms.CharField(label='아이디')
    password = forms.CharField(widget=forms.PasswordInput, label='비밀번호')

def loginView(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('mypage') 
            else:
                form.add_error(None, '아이디 또는 비밀번호가 올바르지 않습니다.')
    else:
        form = Login()
    
    return render(request, 'accounts/login.html', {'form': form})
#회원 정보 수정
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'receive_event']
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('mypage')
    else:
        form = UserUpdateForm(instance=request.user)
    
    return render(request, 'accounts/edit_profile.html', {'form': form})