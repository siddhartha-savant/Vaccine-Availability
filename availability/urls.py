from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getdistrict/', views.getdistrict, name='get_district')

]