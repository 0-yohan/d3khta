from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('poets/', views.all_poets, name = 'poets'),
    path('poets/<int:id>', views.details, name = 'details')
]
