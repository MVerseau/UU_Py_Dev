from django.shortcuts import render
from .forms import UserRegister


def user_generator():
    users = {
        'user1': {'password': 'password1', 'age': "age1"},
        'user2': {'password': 'password2', 'age': "age2"},
        'user3': {'password': 'password3', 'age': "age3"},
        'user4': {'password': 'password4', 'age': "age4"},
        'user5': {'password': 'password5', 'age': "age5"},
    }
    return users

def sign_up_by_django(request):
    template_name = r'fifth_task\registration_page.html'
    users = user_generator()
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.cleaned_data['name']
            password = form.cleaned_data['password']
            pass_repeat = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])
            if user in users:
                info.setdefault('error', 'Пользователь уже существует')
            elif password != pass_repeat:
                info.setdefault('error', 'Пароли не совпадают.')
            elif age < 18:
                info.setdefault('error', 'Вы должны быть старше 18.')
            else:
                success = f'Приветствуем, {user}!'
                info.setdefault('success', success)
    else:
        form = UserRegister()
    info.setdefault('form', form)
    return render(request, template_name, info)


# def sign_up_by_html(request):
#     template_name = r'fifth_task\registration_page.html'
#     info = {}
#     if request.method == 'POST':
#         users = user_generator()
#         user = request.POST.get('name')
#         password = request.POST.get('password')
#         pass_repeat = request.POST.get('repeat_password')
#         age = int(request.POST.get('age'))
#         if user in users:
#             info.setdefault('error', 'Пользователь уже существует')
#         elif password != pass_repeat:
#             info.setdefault('error', 'Пароли не совпадают.')
#         elif age < 18:
#             info.setdefault('error', 'Вы должны быть старше 18.')
#         else:
#             success = f'Приветствуем, {user}!'
#             info.setdefault('success', success)
#
#     return render(request, template_name, context=info)