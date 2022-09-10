from django.db import models


class ArticleChoice(models.TextChoices):
    NEWS = 'news', 'Новости'
    COMMERCIAL = 'commercial', 'Коммерческая'
    BLOG = 'blog', 'Блог'


class Article(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Наименование'
    )
    type = models.CharField(
        choices=ArticleChoice.choices,
        default=ArticleChoice.COMMERCIAL.value,
        max_length=255,
        verbose_name='Тип/Вид'
    )
    text = models.TextField(
        null=True,
        blank=True,
        verbose_name='Текст'
    )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class ArticleFile(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        verbose_name='Статья',
        related_name='files'
    )
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='NAME'
    )
    file = models.FileField(
        upload_to='articles_files/',
        verbose_name='Файл'
    )

    class Meta:
        verbose_name = 'Файл Статьи'
        verbose_name_plural = 'Файлы Статей'


