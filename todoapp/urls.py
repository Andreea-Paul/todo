from django.urls import path
from .views import delete_task, edit_task, home, login_view, logout_view, mark_complete, mark_incomplete,change_password, signup

urlpatterns = [
    path('home', home, name='home'),
    path('delete/<int:todo_id>', delete_task, name='delete'),
    path('mark_complete/<int:todo_id>', mark_complete, name="mark_complete"),
    path('mark_incomplete/<int:todo_id>', mark_incomplete, name="mark_incomplete"),
    path('edit/<int:todo_id>', edit_task, name="edit"),
    path('', login_view, name="login" ),
    path('logout', logout_view, name="logout"),
    path('password', change_password, name='change_password'),
    path('signup', signup, name='signup'),
]
