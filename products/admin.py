from django.contrib import admin

from products.models import Book, Laptop


admin.site.register(Book)
admin.site.register(Laptop)
