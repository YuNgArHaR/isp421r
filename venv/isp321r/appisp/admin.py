from django.contrib import admin
from appisp.models import AboutInfo, AboutImg, Student, New
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(AboutInfo)
admin.site.register(AboutImg)
admin.site.register(Student)
admin.site.register(New)
