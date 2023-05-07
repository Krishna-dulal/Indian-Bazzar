from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('bazzar/', include('bazzar.urls')),
    path('admin/', admin.site.urls),
]