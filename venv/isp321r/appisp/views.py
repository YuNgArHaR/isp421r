from django.shortcuts import render, redirect
from django.urls import reverse
from appisp.models import AboutInfo, AboutImg, Student, New
from django.contrib.auth import authenticate, login, logout
from appisp.forms import *

def index_page(request):
    about_info = AboutInfo.objects.all()
    new = New.objects.order_by('-date')
    return render(request, 'index.html', {'new': new, 'about_info': about_info})

def about_page(request):
    about_info = AboutInfo.objects.all()
    about_img = AboutImg.objects.all()
    return render(request, 'about.html', {'about_info': about_info, 'about_img': about_img})

def students_page(request):
    about_info = AboutInfo.objects.all()
    student = Student.objects.all()
    line1 = Student.objects.filter(line=1)
    line2 = Student.objects.filter(line=2)
    line3 = Student.objects.filter(line=3)
    line4 = Student.objects.filter(line=4)
    line5 = Student.objects.filter(line=5)
    linekyr = Student.objects.filter(line=6)
    return render(request, 'students.html', context={'line1': line1, 'line2': line2, 'line3': line3, 'line4': line4, 'line5': line5, 'linekyr': linekyr, 'about_info': about_info})

def login_page(request):
    about_info = AboutInfo.objects.all()
    return render(request, 'login.html', {'about_info': about_info})


def account_page(request):
    about_info = AboutInfo.objects.all()
    if request.method == 'POST':
        if 'AddNew' in request.POST:
            form = AddNewForm(request.POST, request.FILES)
            if form.is_valid():
                # Получение данных из формы
                name = form.cleaned_data['name']
                date = form.cleaned_data['date']
                img = form.cleaned_data['img']
                info = form.cleaned_data['info']

                # Преобразование информации с отступами
                formatted_info = info.replace('\n', '<br>')  # Замена символов новой строки на тег <br>

                # Создание и сохранение нового объекта
                new = form.save(commit=False)
                new.info = formatted_info  # Записываем отформатированную информацию в поле модели
                new.save()

                return redirect('account')

    else:
        form = AddNewForm()

    return render(request, 'account.html', {'form': form, 'about_info': about_info})

def base_page(request):
    about_info = AboutInfo.objects.all()
    return render(request, 'base.html', {'about_info': about_info})

def admin_login(request):
    return redirect('index')

def admin_logout(request):
    logout(request)
    return redirect('index')