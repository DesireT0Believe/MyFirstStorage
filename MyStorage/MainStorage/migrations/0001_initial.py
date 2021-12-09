# Generated by Django 3.2.9 on 2021-12-02 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SaveFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('saveFile', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('file_describe', models.CharField(default='SOME STRING', max_length=255, verbose_name='Описание')),
                ('time_save', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Файлы на хранении',
                'verbose_name_plural': 'Файлы на хранении',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_login', models.CharField(max_length=16, verbose_name='Логин пользователя')),
                ('user_password', models.CharField(max_length=16, verbose_name='Пароль')),
                ('user_mail', models.EmailField(max_length=254, verbose_name='email')),
            ],
        ),
    ]
