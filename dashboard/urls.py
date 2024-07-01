from django.urls import path
from . import views

urlpatterns = [
     #dashboard
    path('dashboard',views.index,name ='dashboard'),
    
    #staff
    path('staff',views.staff,name ='dashboard-staff'),
    path('staff/detail/<int:pk>/',views.staff_detail,name ='dashboard-staff-detail'),
    
    #cars
    path('cars',views.cars,name ='dashboard-cars'),
    path('cars/delete/<int:pk>/', views.cars_delete,
         name='dashboard-cars-delete'),
    path('cars/edit/<int:pk>/', views.cars_edit,
         name='dashboard-cars-edit'),
    #booking
    path('bookings',views.bookings,name ='dashboard-bookings'),
    
    #client
    path('clients',views.clients,name ='dashboard-clients'),
    path('clients/delete/<int:pk>/', views.clients_delete,
         name='dashboard-clients-delete'),
    path('clients/edit/<int:pk>/', views.clients_edit,
         name='dashboard-clients-edit'),
]