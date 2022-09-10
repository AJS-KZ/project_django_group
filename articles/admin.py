from django.contrib import admin

from articles.models import Article, ArticleFile


admin.site.register(Article)
admin.site.register(ArticleFile)
