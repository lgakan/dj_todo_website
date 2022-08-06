from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('details/', views.details, name='details'),

    path('add_task/', views.add_user, name='add_task'),
    path('delete_task/<str:pk>', views.delete_task, name='delete_task'),
    path('edit_task/<str:pk>', views.edit_task, name='edit_task'),
]
