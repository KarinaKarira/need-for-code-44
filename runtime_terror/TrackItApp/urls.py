from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('report/',views.show),
    # path('second/',views.second,name='second'),
    path('fetch',views.fetch,name='fetch')
]
