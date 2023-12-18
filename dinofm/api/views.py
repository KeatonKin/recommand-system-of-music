from django.contrib.auth import authenticate
from django.http import JsonResponse


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 使用 Django 内置的 authenticate 函数进行身份验证
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # 登录成功
            return JsonResponse({'message': '登录成功'})
        else:
            # 登录失败
            return JsonResponse({'message': '登录失败，请检查用户名和密码。'}, status=400)