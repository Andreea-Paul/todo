from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200) 

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name  


class Todo(models.Model):
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    user  = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    due_date = models.DateField(null=True, blank= True)
    


    class Meta:
        ordering = ("-created", )

    def __str__(self):
        return self.task

    