from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('event/', include('baekjoon.urls')),
    path('', include('common.urls')),
    path('board',include('board.urls')),
]
