import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SaveFile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField("Наименование", max_length=255)
    saveFile = models.FileField("Файл", upload_to='uploads/%Y/%m/%d/')
    file_describe = models.CharField("Описание", max_length=255, blank=True, null=True)
    time_save = models.DateTimeField("Дата загрузки", auto_now_add=True)
    time_update = models.DateTimeField("Дата редактирования", auto_now=True)

    def filename(self):
        return os.path.basename(self.saveFile.name)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Файлы на хранении'
        verbose_name_plural = 'Файлы на хранении'