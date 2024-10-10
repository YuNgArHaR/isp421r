from django.db import models

# Create your models here.
class AboutInfo(models.Model):
    name = models.CharField(max_length=8, blank=False)
    info = models.CharField(max_length=650, blank=False)
    icon = models.ImageField(verbose_name='Иконка', blank=False, upload_to='icon/')

class AboutImg(models.Model):
    img1 = models.ImageField(upload_to='aboutslider/')
    img2 = models.ImageField(upload_to='aboutslider/')
    img3 = models.ImageField(upload_to='aboutslider/')

class Student(models.Model):
    img = models.ImageField(upload_to='students/')
    name = models.CharField(max_length=50, blank=False)
    line = models.IntegerField()

    def __str__(self):
        return self.name

class New(models.Model):
    name = models.CharField(verbose_name='Заголовок', max_length=50, blank=False)
    date = models.DateField(verbose_name='Дата', blank=False)
    img = models.ImageField(verbose_name='Картинка', blank=False, upload_to='news/')
    info = models.CharField(verbose_name='Информация', max_length=1500, blank=False)

    def __str__(self):
        return self.name