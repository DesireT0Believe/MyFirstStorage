# Generated by Django 3.2.9 on 2021-12-02 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainStorage', '0003_auto_20211202_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savefile',
            name='file_describe',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание'),
        ),
    ]