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

    def __str__(self):
        return self.title
