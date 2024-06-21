from django.contrib import admin
from django.urls import path, include
from odealapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('contacts/', views.contacts),
    path('developments/', views.developments),
]
