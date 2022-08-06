from django.urls import path
from .views import home_view, todo_list_item, todoitemCreate, delet_item

app_name = 'todoapp'
urlpatterns = [
    path('', home_view, name='home'),
    path('list/', todo_list_item, name='todo_list'),
    path('create/', todoitemCreate, name='create_todo_item'),
    path('<id>/delete/', delet_item, name='delete_todo_item'),
]
