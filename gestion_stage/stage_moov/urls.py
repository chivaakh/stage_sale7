from django.urls import path
from . import views

urlpatterns=[
    path('start_user',views.create_utilisateur, name='create_utilisateur'),
    path('hello',views.hello, name='hello'),
    path('',views.home, name='home'),
    path('interface',views.interface_principal, name='interface_principal'),
    path('create_candidate',views.create_candidate, name='create_candidate'),
    path('services/', views.service_list, name='service_list'),
    path('services/add/', views.service_add, name='service_add'),
    path('services/edit/<int:pk>/', views.service_edit, name='service_edit'),
    path('services/delete/<int:pk>/', views.service_delete, name='service_delete'),
]