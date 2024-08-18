from django.urls import path
from . import views

urlpatterns=[
    path('start_user',views.create_utilisateur, name='create_utilisateur'),
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
    # path('gestion_demandes/', views.gestion_demandes, name='gestion_demandes'),
    # path('accepter_demande/<int:demande_id>/', views.accepter_demande, name='accepter_demande'),
    # path('rejeter_demande/<int:demande_id>/', views.rejeter_demande, name='rejeter_demande'),
    path('deletuser/<int:id_user>/', views.deletuser,name='deletuser'),
    path('show_candidate',views.show_candidate, name='show_candidate'),
    path('delete_candidate/<int:id_candidate>/', views.delete_candidate,name='delete_candidate'),
    path('gestion_demandes/', views.gestion_demandes, name='gestion_demandes'),
    path('accepter_demande/<int:demande_id>/', views.accepter_demande, name='accepter_demande'),
    path('rejeter_demande/<int:demande_id>/', views.rejeter_demande, name='rejeter_demande'),
    path('sujets/', views.liste_sujets, name='liste_sujets'),
    path('sujets/ajouter/', views.ajouter_sujet, name='ajouter_sujet'),
    path('sujets/modifier/<int:pk>/', views.modifier_sujet, name='modifier_sujet'),
    path('sujets/supprimer/<int:pk>/', views.supprimer_sujet, name='supprimer_sujet'),


]