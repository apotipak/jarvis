from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('phone-list', views.PhoneList, name='phone-list'),
    path('staff-profile', views.StaffProfile, name='staff-profile'),
    path('staff-trophy', views.StaffTrophy, name='staff-trophy'),
    path('public-holiday', views.PublicHoliday, name='public-holiday'),    
]
