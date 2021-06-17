from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getdistrict/', views.getdistrict, name='get_district'),
    path('scheduledata/', views.scheduledata, name='schedule_data'),

]