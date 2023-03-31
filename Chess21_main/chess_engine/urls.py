from django.urls import path
from .views import chessboard, make_move

urlpatterns = [
    path('', chessboard, name='chessboard'),
    path('make_move', make_move, name='make_move'),
]
