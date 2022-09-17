from django.db import models


class Laptop(models.Model):
    company = models.CharField(
        max_length=255,
        verbose_name='От компании'
    )
    model = models.CharField(
        verbose_name='Модель',
        max_length=255,
    )
    price = models.IntegerField(
        verbose_name='Стоимость',
        default=0
    )
    weight = models.PositiveIntegerField(
        verbose_name='Вес',
        default=0,
    )

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'