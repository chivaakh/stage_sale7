from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
     # URL pour lister tous les candidats
    path('candidats/', views.liste_candidats, name='liste_candidats'),
    # URL pour envoyer un message à un candidat
    path('candidats/<int:candidat_id>/envoyer-message/', views.envoyer_message, name='envoyer_message'),
    # URL pour afficher les messages pour un candidat
    path('candidats/messages/', views.liste_messages, name='liste_messages'),
     # URL pour afficher les messages pour un utilisateur
     path('chivaa/', views.chivaa, name='chivaa'),
    # URL pour marquer un message comme lu
    path('messages/<int:notification_id>/marquer-comme-lu/', views.marquer_comme_lu, name='marquer_comme_lu'),
    path('start_user',views.create_utilisateur, name='create_utilisateur'),
    path('form_user/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    # path('create_candidate',views.create_candidate, name='create_candidate'),
    path('services/', views.service_list, name='service_list'),
    path('services/', views.service_list, name='service_list_candidat'),
    path('services/add/', views.service_add, name='service_add'),
    path('services/edit/<int:pk>/', views.service_edit, name='service_edit'),
    path('services/delete/<int:pk>/', views.service_delete, name='service_delete'),
    path('enregistrer/', views.enregistrer_candidat, name='enregistrer_candidat'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('form_candidat/', views.form_candidat, name='form_candidat'),
    path('interface',views.interface_principal, name='interface_principal'),
    path('edit_role<int:id_user>',views.modifier_role, name='modifier_role'),
    path('amjhdmin',views.nevbar_admin, name='nevbar_admin'),
    path('RH',views.nevbar_RH, name='nevbar_RH'),
    path('encadreur',views.nevbar_encadreur, name='nevbar_encadreur'),
    path('candidat',views.nevbar_candidat, name='nevbar_candidat'),
    path('login_candidat',views.login_candidat, name='login_candidat'),
    path('logout_candidat',views.logout_candidat, name='logout_candidat'),
    path('deletuser/<int:id_user>/', views.deletuser,name='deletuser'),
    path('show_candidate',views.show_candidate, name='show_candidate'),
    path('delete_candidate/<int:id_candidate>/', views.delete_candidate,name='delete_candidate'),
    path('gestion_demandes/', views.gestion_demandes, name='gestion_demandes'),
   path('accepter_demande/<int:demande_id>/', views.accepter_demande, name='accepter_demande'),
    path('rejeter_demande/<int:demande_id>/', views.rejeter_demande, name='rejeter_demande'),
    path('candidat/inscription/', views.form_candidat, name='create_candidat'),
    path('utilisateur/inscription/', views.create_utilisateur, name='create_utilisateur'),
    path('', views.homepage, name='homepage'),
    path('getMessages/<str:room>/', views.getMessages , name ="getMessages"),
    path('service/<int:service_id>/sujets/', views.liste_sujets_par_service, name='liste_sujets_par_service'),
    path('service/<int:service_id>/sujets/ajouter/', views.ajouter_sujet, name='ajouter_sujet'),
    path('choix_sujet', views.choix_sujet, name='choix_sujet'),
    path('vue_sujets_choisis', views.vue_sujets_choisis, name='vue_sujets_choisis'),
    path('sujets/<int:sujet_id>/modifier/', views.modifier_sujet, name='modifier_sujet'),
    path('sujets/<int:sujet_id>/supprimer/', views.supprimer_sujet, name='supprimer_sujet'),
    path('create_attestation/', views.create_attestation, name='create_attestation'),
    path('list_attestations/', views.list_attestations, name='list_attestations'),
    path('attestation/<int:attestation_id>/download/',views.download_attestation, name='download_attestation'),
    path('enrigstrer/',views.enrigstrer, name='enrigstrer'),
    path('list_rapport/',views.list_rapport, name='list_rapport'),
    path('download_rapport/<int:rapport_id>',views.download_rapport, name='download_rapport'),
    path('service_list_candidat/',views.service_list_candidat, name='service_list_candidat'),
    path('service_list_RH/',views.service_list_RH, name='service_list_RH'),
    path('service_list_encadreur/',views.service_list_encadreur, name='service_list_encadreur'),
  
    path('ev_start', views.start_chat , name ="ev_start"),
    path('<str:room>/', views.room , name ="room"),
    path('checkview', views.checkview , name ="checkview"),
    path('send', views.send , name ="send"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


