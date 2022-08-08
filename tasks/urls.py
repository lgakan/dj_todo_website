from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    # path('login/', views.CustomLoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('home/', views.home, name='home'),
    path('details/', views.details, name='details'),

    path('add_task/', views.add_user, name='add_task'),
    path('delete_task/<str:pk>', views.delete_task, name='delete_task'),
    path('edit_task/<str:pk>', views.edit_task, name='edit_task'),
]
