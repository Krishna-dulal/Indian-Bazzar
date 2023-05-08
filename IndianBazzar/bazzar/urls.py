from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('hours/', views.hours, name='hours'),
]
urlpatterns += staticfiles_urlpatterns()
