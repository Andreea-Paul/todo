from django.urls import path
from .views import delete, home 

urlpatterns = [
    path('home', home, name='home'),
    path('delete/<int:todo_id>', delete, name='delete'),
]