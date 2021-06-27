from django.urls import path
from .views import delete_task, edit_task, home, mark_complete, mark_incomplete 

urlpatterns = [
    path('home', home, name='home'),
    path('delete/<int:todo_id>', delete_task, name='delete'),
    path('mark_complete/<int:todo_id>', mark_complete, name="mark_complete"),
    path('mark_incomplete/<int:todo_id>', mark_incomplete, name="mark_incomplete"),
    path('edit/<int:todo_id>', edit_task, name="edit"),
]
