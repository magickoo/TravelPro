from django.urls import path
from . import views

urlpatterns = [
    path('dashboard',views.index,name ='dashboard'),
    path('staff',views.staff,name ='dashboard-staff'),
    path('clients',views.clients,name ='dashboard-clients'),
    path('bookings',views.bookings,name ='dashboard-bookings'),
    path('clients/delete/<int:pk>/', views.clients_delete,
         name='dashboard-clients-delete'),
    path('clients/edit/<int:pk>/', views.clients_edit,
         name='dashboard-clients-edit'),
]