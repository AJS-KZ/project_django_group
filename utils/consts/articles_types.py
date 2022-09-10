from django.db import models


class ArticleChoice(models.TextChoices):
    NEWS = 'news', 'Новости'
    COMMERCIAL = 'commercial', 'Коммерческая'
    BLOG = 'blog', 'Блог'
