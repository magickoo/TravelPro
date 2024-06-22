from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name ='dashboard'),
    path('staff',views.staff,name ='dashboard-staff'),
    path('clients',views.clients,name ='dashboard-clients'),
    path('bookings',views.bookings,name ='dashboard-bookings'),
]