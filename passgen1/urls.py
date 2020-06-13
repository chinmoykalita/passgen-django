from django.urls import path, include
from . import views
from django.contrib import admin

admin.site.site_header = 'PassGen'                    
admin.site.index_title = 'PassGen administration'                 
admin.site.site_title = 'Welcome to passgen site admin' 

urlpatterns = [
    path('', views.index),
    path('result/', views.result, name="generated"),
    
]
