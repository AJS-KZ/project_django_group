from django.db import models


class Book(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Наименование',
    )
    publish_date = models.DateTimeField(
        verbose_name='Дата публикации на сайте',
        auto_now_add=True,
    )
    price = models.IntegerField(
        verbose_name='Стоимость',
        default=0
    )
    description = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name='Описание'
    )

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        # order = 'publish_date'

    def __str__(self):
        return self.title


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
