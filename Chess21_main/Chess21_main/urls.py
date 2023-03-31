from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_pages.urls')),
    path('chessboard/', include('chess_engine.urls')),
]
