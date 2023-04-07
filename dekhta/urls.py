from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('poets/', views.all_poets, name = 'poets'),
    path('poets/<str:first_name>-<str:last_name>/', views.details, name = 'details'),
    path('create_user/', views.create_user, name = 'create'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),
    path('contact_us/', views.contact, name = 'contact'),
    path('add_post/', views.add_post, name = 'add_post'),
    path('read/', views.read, name = 'read'),
]
