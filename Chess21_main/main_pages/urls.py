from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('chess/', views.chess),
    path('chess2/', views.chess_new),
]
