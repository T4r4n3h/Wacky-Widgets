from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('add/', views.add, name='add'),
    path('<int:wdg_id>/delete/', views.delete, name='delete'),
]