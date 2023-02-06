# Generated by Django 4.1.6 on 2023-02-06 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(verbose_name='关于')),
            ],
        ),
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='地址')),
                ('contact_num', models.IntegerField()),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('content', models.TextField(verbose_name='正文')),
                ('isPublic', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='名字')),
                ('father_name', models.CharField(max_length=100, verbose_name='父亲姓名')),
                ('mother_name', models.CharField(max_length=100, verbose_name='母亲姓名')),
                ('gender', models.CharField(default='male', max_length=50, verbose_name='性别')),
                ('address', models.CharField(max_length=100, verbose_name='地址')),
                ('city', models.CharField(max_length=50, verbose_name='城市')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('contact_num', models.IntegerField(default=1234657, verbose_name='联系号码')),
                ('date_of_birth', models.DateField(max_length=50, verbose_name='出生日期')),
                ('course', models.CharField(max_length=50, verbose_name='课程')),
                ('stu_id', models.CharField(max_length=50, verbose_name='学号')),
                ('user_name', models.CharField(max_length=50, verbose_name='用户名')),
                ('password', models.CharField(max_length=100, verbose_name='用户名')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='姓名')),
                ('gender', models.CharField(max_length=50, verbose_name='性别')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('contact_num', models.CharField(max_length=20)),
                ('qualification', models.TextField(verbose_name='资质')),
            ],
        ),
    ]
