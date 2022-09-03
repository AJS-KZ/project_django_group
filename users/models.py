from django.db import models


class User(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='Полное имя')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.full_name
