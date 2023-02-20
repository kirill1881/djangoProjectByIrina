from django.db import models


class Task(models.Model):
    name = models.CharField('task_name',max_length=255)
    text = models.TextField('text')
    time = models.IntegerField('time')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'