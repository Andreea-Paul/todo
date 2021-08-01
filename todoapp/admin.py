from django.contrib import admin
from .models import Category, Todo

# Register your models here.
admin.site.register(Todo)
admin.site.register(Category)