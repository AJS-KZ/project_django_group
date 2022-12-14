# Generated by Django 4.1 on 2022-09-10 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('type', models.CharField(choices=[('news', 'Новости'), ('commercial', 'Коммерческая'), ('blog', 'Блог')], max_length=255, verbose_name='Тип/Вид')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='ArticleFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='articles_files/', verbose_name='Файл')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='articles.article', verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Файл Статьи',
                'verbose_name_plural': 'Файлы Статей',
            },
        ),
    ]
