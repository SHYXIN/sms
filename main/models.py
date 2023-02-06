from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class AboutPage(models.Model):
    about = models.TextField(verbose_name='关于')

    def __str__(self):
        return self.about


class ContactPage(models.Model):
    address = models.TextField(verbose_name='地址')
    contact_num = models.IntegerField()
    email = models.EmailField(verbose_name='邮箱')

    def __str__(self):
        return self.address


class Student(models.Model):
    full_name = models.CharField(verbose_name='名字', max_length=100)
    father_name = models.CharField(verbose_name='父亲姓名', max_length=100)
    mother_name = models.CharField(verbose_name='母亲姓名', max_length=100)
    gender = models.CharField(verbose_name='性别', max_length=50, default='male')
    address = models.CharField(verbose_name='地址',max_length=100)
    city = models.CharField(verbose_name='城市',max_length=50)
    email = models.EmailField(verbose_name='邮箱')
    contact_num = models.IntegerField(verbose_name='联系号码',default=1234657)
    date_of_birth = models.DateField(verbose_name='出生日期',max_length=50)
    course = models.CharField(verbose_name='课程',max_length=50)
    stu_id = models.CharField(verbose_name='学号',max_length=50)
    user_name = models.CharField(verbose_name='用户名', max_length=50)
    password = models.CharField(verbose_name='用户名',max_length=100)

    def __str__(self):
        return self.full_name

class Notice(models.Model):
    title = models.CharField(verbose_name='标题',max_length=200)
    content = models.TextField(verbose_name='正文')
    isPublic = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Teacher(models.Model):
    full_name = models.CharField(verbose_name='姓名',max_length=100)
    gender= models.CharField(verbose_name='性别', max_length=50)
    email = models.EmailField(verbose_name='邮箱')
    contact_num = models.CharField(max_length=20)
    qualification = models.TextField(verbose_name='资质')

    def __str__(self):
        return self.full_name
