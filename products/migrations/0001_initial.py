# Generated by Django 4.1 on 2022-09-03 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('publish_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации на сайте')),
                ('price', models.IntegerField(default=0, verbose_name='Стоимость')),
                ('description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=255, verbose_name='От компании')),
                ('model', models.CharField(max_length=255, verbose_name='Модель')),
                ('price', models.IntegerField(default=0, verbose_name='Стоимость')),
                ('weight', models.PositiveIntegerField(default=0, verbose_name='Вес')),
            ],
        ),
    ]
