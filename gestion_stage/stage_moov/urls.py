from django.urls import path
from . import views

urlpatterns=[
    path('start_user',views.create_utilisateur, name='create_utilisateur'),
    path('hello',views.hello, name='hello'),
    path('',views.login, name='home'),
    path('create_candidate',views.create_candidate, name='create_candidate'),
    path('services/', views.service_list, name='service_list'),
    path('services/add/', views.service_add, name='service_add'),
    path('services/edit/<int:pk>/', views.service_edit, name='service_edit'),
    path('services/delete/<int:pk>/', views.service_delete, name='service_delete'),
    path('notifications/', views.notifications_view, name='notifications'),
    path('enregistrer/', views.enregistrer_candidat, name='enregistrer_candidat'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('form_candidat/', views.form_candidat, name='form_candidat'),
    path('interface',views.interface_principal, name='interface_principal'),
    path('deletuser/<int:id_user>/', views.deletuser,name='deletuser'),
    path('show_candidate',views.show_candidate, name='show_candidate'),
    path('delete_candidate/<int:id_candidate>/', views.delete_candidate,name='delete_candidate'),
<<<<<<< HEAD
    # path('gestion_demandes/', views.gestion_demandes, name='gestion_demandes'),
    # path('accepter_demande/<int:demande_id>/', views.accepter_demande, name='accepter_demande'),
    # path('rejeter_demande/<int:demande_id>/', views.rejeter_demande, name='rejeter_demande'),
=======
    path('gestion_demandes/', views.gestion_demandes, name='gestion_demandes'),
    path('accepter_demande/<int:demande_id>/', views.accepter_demande, name='accepter_demande'),
    path('rejeter_demande/<int:demande_id>/', views.rejeter_demande, name='rejeter_demande'),
>>>>>>> 6702d40c70e612a14f1944d1b73bae750fa905d3
]