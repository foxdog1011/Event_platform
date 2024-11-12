from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Success !! {username}！')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def profile(request):
    if request.method == 'POST':
        # 创建用于更新用户资料的表单
        pass  # 您需要创建表单类，并处理表单提交
    else:
        pass  # 显示用户资料
    return render(request, 'users/profile.html')

