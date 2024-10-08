from django.shortcuts import render, redirect,get_object_or_404
from .forms import ServiceForm,SujetStageForm
from .models import *
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Service,Utilisateur,Candidats,Demandes
from django.db.models import Q
from .models import Notification
from .forms import CandidatForm
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.http import HttpResponse , JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
import logging
from .models import Sujet_stage
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import SujetStageForm  # Assume que tu as un formulaire pour Sujet_stage
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Affectation, Demandes, Sujet_stage
from django.contrib.auth.hashers import check_password

# Create your views here.
#les views pour gestions des utilisateur

from django.shortcuts import render, get_object_or_404, redirect
from .models import Candidats, Notification

def liste_candidats(request):
    candidats = Candidats.objects.all()
    return render(request, 'utilisateur/liste_candidats.html', {'candidats': candidats})

logger = logging.getLogger(__name__)

@login_required

def envoyer_message(request, candidat_id):
    candidat = get_object_or_404(Candidats, pk=candidat_id)

    if request.method == 'POST':
        message = request.POST.get('message')

        # Récupérer les informations de l'utilisateur à partir de la session
        utilisateur_email = request.session.get('user_email')
        utilisateur_role = request.session.get('user_role')

        if not utilisateur_email or not utilisateur_role:
            return render(request, 'sidebar/error.html', {'error_message': "Vous n'êtes pas connecté."})

        try:
            utilisateur = Utilisateur.objects.get(Email=utilisateur_email)
        except Utilisateur.DoesNotExist:
            return render(request, 'sidebar/error.html', {'error_message': "Utilisateur non trouvé."})

        # Vérifier que l'utilisateur a le rôle 'Encadreur'
        if utilisateur.role != 'Encadreur':
            return render(request, 'sidebar/error.html', {'error_message': "Vous n'êtes pas autorisé à envoyer des messages."})

        # Créer la notification
        notification = Notification.objects.create(
            message=message,
            utilisateur=utilisateur,
            candidat=candidat
        )
        notification.save()

        # Ajouter un message de succès
        messages.success(request, 'Le message a été envoyé avec succès.')

        return render(request, 'utilisateur/envoyer_message.html', {'candidat': candidat})

    return render(request, 'utilisateur/envoyer_message.html', {'candidat': candidat})

#liste message pour les encadreurs
def chivaa(request):
    # Assurez-vous que l'utilisateur est connecté
    if not request.user.is_authenticated:
        return redirect('login')  # Redirige vers la page de connexion si non connecté

    # Récupérez l'utilisateur connecté à partir de la session
    email = request.session.get('user_email')
    utilisateur = Utilisateur.objects.filter(Email=email).first()
    
    if utilisateur is None:
        return render(request, 'sidebar/error.html', {'error_message': "Utilisateur non trouvé."})

    # Assurez-vous que l'utilisateur a le rôle "Encadreur"
    if utilisateur.role != 'Encadreur':
        return render(request, 'sidebar/error.html', {'error_message': "Vous n'avez pas l'autorisation de voir ces messages."})

    # Filtrez les notifications envoyées par l'encadreur connecté
    notifications = Notification.objects.filter(utilisateur=utilisateur)

    return render(request, 'utilisateur/liste_messages_chiva.html', {'notifications': notifications})


#liste message pour les candidat
from django.shortcuts import get_object_or_404

def liste_messages(request):
    utilisateur_connecte = request.user
    print(f"Utilisateur Django connecté : {utilisateur_connecte}")

    try:
        utilisateur_personnalise = Utilisateur.objects.get(Id_utilisateur=utilisateur_connecte.id)
        print(f"Utilisateur personnalisé trouvé : {utilisateur_personnalise}")

        # Vérifiez toutes les instances de Candidats associées à cet utilisateur
        candidats_associes = Candidats.objects.filter(Id_utilisateur=utilisateur_personnalise)
        print(f"Candidats associés trouvés : {candidats_associes}")

        if candidats_associes.exists():
            candidat_connecte = candidats_associes.first()  # Choisir le premier candidat associé
            print(f"Candidat connecté : {candidat_connecte}")

            notifications = Notification.objects.filter(candidat=candidat_connecte)
            print(f"Notifications trouvées : {notifications}")
        else:
            notifications = Notification.objects.none()
            print("Aucun candidat trouvé pour cet utilisateur.")

    except Utilisateur.DoesNotExist:
        print("Utilisateur personnalisé non trouvé.")
        notifications = Notification.objects.none()

    return render(request, 'utilisateur/liste_messages.html', {'notifications': notifications})





def marquer_comme_lu(request, notification_id):
    notification = get_object_or_404(Notification, pk=notification_id)
    notification.lu = True
    notification.save()
    return redirect('liste_messages')


def create_utilisateur(request):
    if request.method == 'POST':
        nom_complet = request.POST.get('Nom_complet')
        email = request.POST.get('Email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        # Validation des données
        if not (nom_complet and email and password and role):
            messages.error(request, 'Tous les champs doivent être remplis.')
            return redirect('create_utilisateur')

        # Vérification si l'email est déjà utilisé
        if Utilisateur.objects.filter(Email=email).exists():
            messages.error(request, 'Un utilisateur avec cet email existe déjà.')
            return redirect('create_utilisateur')

        # Hachage du mot de passe
        hashed_password = make_password(password)

        # Création et sauvegarde de l'utilisateur
        Utilisateur.objects.create(
            Nom_complet=nom_complet,
            Email=email,
            password=hashed_password,
            role=role
        )

        messages.success(request, 'Utilisateur créé avec succès.')
        return redirect('login')

    return render(request, 'gestions_users/home.html')
#fonction pour la login
def login(request):
    error_message = None

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email and password:
            utilisateur = Utilisateur.objects.filter(Email=email).first()
            if utilisateur and utilisateur.check_password(password):
                request.session['user_email'] = utilisateur.Email
                request.session['user_role'] = utilisateur.role
                request.session['user_name'] = utilisateur.Nom_complet 
                if utilisateur and utilisateur.role == 'Admin':
                    return redirect('nevbar_admin') 
                elif utilisateur and utilisateur.role == 'RH':
                     return redirect('nevbar_RH') 
                elif utilisateur and utilisateur.role == 'Encadreur':
                     return redirect('nevbar_encadreur') 
            else:
                error_message = "Email ou mot de passe incorrect."
        else:
            error_message = "Veuillez remplir tous les champs."

    user = request.user
    utilisateur_exists = Utilisateur.objects.filter(Email=user.email).exists() if user.is_authenticated else False

    return render(request, 'gestions_users/home.html', {
        'user': user,
        'utilisateur_exists': utilisateur_exists,
        'error_message': error_message,
    })


def logout(request):
    return redirect('login')
#les views pour les creet de candidat
def login_candidat(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('Password')
        candidats = Candidats.objects.filter(email=email)
        
        if candidats.exists():
            candidat = candidats.first()

            # Vérifier si la demande du candidat a été acceptée
            demande = Demandes.objects.filter(Nom_candidat=candidat, statut='accepté').first()

            if demande:
                if password == candidat.password:
                    # Stocker les informations du candidat dans la session
                    request.session['candidat_email'] = candidat.email
                    request.session['candidat_nom_complet'] = candidat.Nom_complet  
                    request.session['candidat_id'] = candidat.Id_candidat
                
                    return redirect('nevbar_candidat')
                else:
                    return render(request, 'Candidats/login.html', {'error': 'Mot de passe incorrect'})
            else:
                return render(request, 'Candidats/login.html', {'error': 'Votre demande de stage n\'a pas encore été acceptée'})
        else:
            return render(request, 'Candidats/login.html', {'error': 'Email non trouvé'})

    return render(request, 'Candidats/login.html', {'login_candidat': 'login_candidat'})


def logout_candidat(request):
    return redirect('login_candidat')

#les fonction CRUD pour gestions les utilisateurs
def interface_principal(request):
    query = request.GET.get('cherch')
    if query:
        utilisateur=Utilisateur.objects.filter(
            Q(Id_utilisateur__icontains=query)|
            Q(Nom_complet__icontains=query)|
            Q(role__icontains=query)|
            Q(Email__icontains=query)|
            Q(Date_creation__icontains=query)
        )
    else:
        utilisateur=Utilisateur.objects.all()
    return render(request,'gestions_users/Interface_principale.html',{'utilisateur': utilisateur} )
def modifier_role(request, id_user):
    utilisateur = get_object_or_404(Utilisateur, Id_utilisateur=id_user)
    if request.method == 'POST':
        nouveau_role = request.POST.get('role')
        if nouveau_role:
            utilisateur.role = nouveau_role
            utilisateur.save()
            messages.success(request, "Le rôle a été mis à jour avec succès.")
            return redirect('interface_principal') 
        else:
            messages.error(request, "Veuillez sélectionner un rôle valide.")
    return redirect('interface_principal') 
def deletuser(request, id_user):
    utilisateur = Utilisateur.objects.filter(Id_utilisateur=id_user).first()  
    if utilisateur: 
        utilisateur.delete()  
    return redirect('interface_principal') 
# les nevbars:
def nevbar_admin(request):
    return render(request,'sidebar/nevbar_admin.html')
def nevbar_RH(request):
    return render(request,'sidebar/nevbar_RH.html')
def nevbar_encadreur (request):
    return render(request,'sidebar/nevbar_encadreur.html')
def nevbar_candidat (request):
    return render(request,'sidebar/nevbar_candidat.html')


#RD pour la candidat
def show_candidate(request):
    query = request.GET.get('cherch')
    if query:
        candidate=Candidats.objects.filter(
            Q(Nom_complet__icontains=query)|
            Q(universite__icontains=query)|
            Q(niveau_academique__icontains=query)|
            Q(specialite__icontains=query)|
            Q(Date_Naissance__icontains=query)|
            Q(telephone__icontains=query)|
            Q(periode__icontains=query)
        )
    else:
       candidate=Candidats.objects.all()
    return render(request,'Candidats/show_candidat.html',{'candidate':candidate})

def delete_candidate(request,id_candidate):
    candidate=Candidats.objects.filter(Id_candidat=id_candidate).first()
    if candidate:
        candidate.delete()
    return redirect('show_candidate')

#pour gestion des demandes
def gestion_demandes(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    query = request.GET.get('cherch', '')
    
    if query:
        demandes = Demandes.objects.filter(
            Q(Nom_candidat__Nom_complet__icontains=query) |
            Q(statut__icontains=query) |
            Q(Date_soumission__icontains=query)
        )
    else:
        demandes = Demandes.objects.all()
    
    return render(request, 'gestion_demande/gestion_demandes.html', {'demandes': demandes})
#les views pour accepter
def accepter_demande(request, demande_id):
   demande = Demandes.objects.filter(Id_demande=demande_id).first()
   demande.statut = 'accepté'
   demande.save()
   return redirect('gestion_demandes')

#pour la rejet
def rejeter_demande(request, demande_id):
    demande = Demandes.objects.filter(Id_demande=demande_id).first()
    demande.statut = 'rejete'
    demande.save()
    return redirect('gestion_demandes')
#les views pour la service
def service_list(request):
    user_email = request.session.get('user_email')
    utilisateur = Utilisateur.objects.filter(Email=user_email).first()
    # user=Utilisateur.objects.filter(Utilisateur.role).first
    query = request.GET.get('q')
    if query:
        services = Service.objects.filter(Nom_service__icontains=query)
    else:
        services = Service.objects.all()
    
    return render(request, 'Service/service_list.html', {'services': services, 'query': query, 'utilisateur':utilisateur})
# Rest of your views...
def service_add(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'Service/service_add.html', {'form': form})

def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'Service/service_edit.html', {'form': form, 'service': service})

def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    return render(request, 'service/service_delete.html', {'service': service})

def enregistrer_candidat(request):
    if request.method == 'POST':
        form = CandidatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Le candidat a été enregistré avec succès.')
    else:
        form = CandidatForm()
    
    return render(request, 'Candidats/candidats.html', {'form': form})

def confirmation(request):
    return render(request, 'Candidats/confirmation.html')

def form_candidat(request):
    return render(request, 'Candidats/code.html')

# Liste des sujets par service
def liste_sujets_par_service(request, service_id):
    service = get_object_or_404(Service, Id_service=service_id)
    sujets = Sujet_stage.objects.filter(Id_service=service)
    
    # Ajouter service_id au contexte pour utilisation dans le template
    return render(request, 'sujets/liste_par_service.html', {'sujets': sujets,'service':service, 'service_id': service_id})



# Ajouter un sujet
def ajouter_sujet(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    if request.method == 'POST':
        form = SujetStageForm(request.POST)
        if form.is_valid():
            sujet = form.save(commit=False)
            sujet.Id_service = service  # Associe le sujet au service
            sujet.save()
            return redirect('liste_sujets_par_service', service_id=service.Id_service)
    else:
        form = SujetStageForm()

    return render(request, 'sujets/ajouter.html', {'form': form, 'service': service})

# Modifier un sujet

def modifier_sujet(request, sujet_id):
    sujet = get_object_or_404(Sujet_stage, pk=sujet_id)
    if request.method == 'POST':
        form = SujetStageForm(request.POST, instance=sujet)
        if form.is_valid():
            form.save()
            return redirect('liste_sujets_par_service', service_id=sujet.Id_service.Id_service)
    else:
        form = SujetStageForm(instance=sujet)
    return render(request, 'sujets/modifier.html', {'form': form, 'sujet': sujet, 'service': sujet.Id_service})



# Supprimer un sujet

def supprimer_sujet(request, sujet_id):
    sujet = get_object_or_404(Sujet_stage, pk=sujet_id)
    if request.method == 'POST':
        service_id = sujet.Id_service.Id_service  # Utilise Id_service pour accéder à l'ID
        sujet.delete()
        return redirect('liste_sujets_par_service', service_id=service_id)
    return render(request, 'sujets/confirm_delete.html', {'sujet': sujet})




def homepage(request):
    return render(request, 'first/code.html')

#les view pour evaluation
def start_chat(request):
    return render(request, 'evaluation/noveau_evaluation.html')

def room(request , room):
    username = request.GET.get('username')
    room_details = get_object_or_404(Room, name=room)
    return render(request , 'evaluation/room.html' , {
        'username' : username ,
        'room' : room ,
        'room_details' : room_details
    })
def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name = room).exists():
        return redirect('/'+ room + '/?username=' + username)
    else:
        new_room = Room.objects.create(name = room)
        new_room.save()
        return redirect('/'+ room + '/?username=' + username)
    

def send(request):
    if request.method == 'POST':
        message = request.POST['message']
        username = request.POST['username']
        room_Id = request.POST['room_id']  
        file=request.FILES.get('file')
  
        room = Room.objects.get(id=room_Id)
        if file:
                new_message = Evaluation.objects.create(content=message, user=username, room=room, files=file)
        else:
                new_message = Evaluation.objects.create(content=message, user=username, room=room)
        new_message.save()
        return JsonResponse({'status': 'Message envoyé avec succès!'})
    return JsonResponse({'status': 'Requête invalide'}, status=400)

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Evaluation.objects.filter(room=room_details.id).order_by('date')
    messages_list = []

    for message in messages:
        message_data = {
            'content': message.content,
            'user': message.user,
            'date': message.date.isoformat(),
            'files': message.files.url if message.files else None
        }
        messages_list.append(message_data)

    return JsonResponse({"messages": messages_list})
#pour le rapport:
# def rapport(request):
#     return render(request,'Candidats/rapport.html')
def list_rapport(request):
    rapports = Document.objects.all()
    return render(request, 'Candidats/list_rapport.html', {'rapports': rapports})

def enrigstrer(request):
    if request.method == 'POST':
        user_email = request.session.get('candidat_email') 
        candidat=Candidats.objects.filter(email=user_email).first()
        id_demande=Demandes.objects.filter(Nom_candidat=candidat).first()
        file = request.FILES['document_file']
        document = Document(
                    candidat=candidat,
                    Id_demande=id_demande,
                    chemin_document=file
                )
        document.save()
    return render(request,'Candidats/rapport.html')
def download_rapport(request, rapport_id):
    rapport = get_object_or_404(Document, pk=rapport_id)
    file_path = rapport.chemin_document.path 

    if not os.path.exists(file_path):
        raise Http404("File not found")

    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename= rapport.chemin_document.name)




from .models import Attestation


def create_attestation(request):
    candidats = Candidats.objects.all()
    affectation = Affectation.objects.all()
    
    if request.method == 'POST':
        # Récupération des données du formulaire
        Id_affectation = request.POST.get('Id_affectation')
        stagaire_id = request.POST.get('stagaire')
        chemin_attestation = request.FILES.get('chemin_attestation')

        # Vérification de la présence des données nécessaires
        if Id_affectation and stagaire_id and chemin_attestation:
            # Création d'une nouvelle instance d'Attestation
            attestation = Attestation(
                Id_affectation=Affectation.objects.get(Id_affectation=Id_affectation),
                stagaire=Candidats.objects.get(Id_candidat=stagaire_id),
                chemin_attestation=chemin_attestation
            )
            attestation.save()
            return redirect('success_page') 
        else:
            print("Données manquantes ou invalides")

    return render(request, 'Candidats/attestation.html', {'candidats': candidats, 'affectation': affectation})


def list_attestations(request):
    user_email = request.session.get('candidat_email') 
    candidat=Candidats.objects.filter(email=user_email).first()
    attestations = Attestation.objects.filter(stagaire=candidat.Id_candidat)

    return render(request, 'Candidats/exporter_attes.html', {'attestations': attestations})



from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from .models import Attestation
import os

def download_attestation(request, attestation_id):
    attestation = get_object_or_404(Attestation, pk=attestation_id)
    file_path = attestation.chemin_attestation.path 

    if not os.path.exists(file_path):
        raise Http404("File not found")

    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=attestation.chemin_attestation.name)

#for show les services candidat
def service_list_candidat(request):
    user_email = request.session.get('user_email') 
    utilisateur = Utilisateur.objects.filter(Email=user_email).first()
    # user=Utilisateur.objects.filter(Utilisateur.role).first
    query = request.GET.get('q')
    if query:
        services = Service.objects.filter(Nom_service__icontains=query)
    else:
        services = Service.objects.all()
    
    return render(request, 'Service/service_candidat.html', {'services': services, 'query': query, 'utilisateur':utilisateur})


def service_list_RH(request):
    user_email = request.session.get('user_email') 
    utilisateur = Utilisateur.objects.filter(Email=user_email).first()
    # user=Utilisateur.objects.filter(Utilisateur.role).first
    query = request.GET.get('q')
    if query:
        services = Service.objects.filter(Nom_service__icontains=query)
    else:
        services = Service.objects.all()
    
    return render(request, 'Service/service_RH.html', {'services': services, 'query': query, 'utilisateur':utilisateur})

def service_list_encadreur(request):
    user_email = request.session.get('user_email') 
    utilisateur = Utilisateur.objects.filter(Email=user_email).first()
    # user=Utilisateur.objects.filter(Utilisateur.role).first
    query = request.GET.get('q')
    if query:
        services = Service.objects.filter(Nom_service__icontains=query)
    else:
        services = Service.objects.all()
    
    return render(request, 'Service/service_encadreur.html', {'services': services, 'query': query, 'utilisateur':utilisateur})
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Sujet_stage, Service, Candidats, Affectation, Demandes

# def choix_sujet(request):
#     # Récupérer tous les sujets
#     sujets = Sujet_stage.objects.all()
#     services = Service.objects.all()

#     # Filtrage par service
#     service_id = request.GET.get('service')
#     if service_id:
#         sujets = sujets.filter(Id_service=service_id)

#     # Recherche par titre ou description
#     query = request.GET.get('query')
#     if query:
#         sujets = sujets.filter(Q(titre__icontains=query) | Q(description__icontains=query))

#     # Lorsqu'un stagiaire choisit un sujet
#     if request.method == "POST":
#         sujet_id = request.POST.get('sujet_id')
#         sujet = get_object_or_404(Sujet_stage, pk=sujet_id)
#         candidat = Candidats.objects.get(Id_utilisateur=request.user.utilisateur)  # Assure-toi que le candidat est récupéré correctement.
#         demande = Demandes.objects.get(Nom_candidat=candidat)  # Supposons que chaque candidat a une seule demande.
        
#         # Créer une affectation pour ce sujet et ce candidat
#         Affectation.objects.create(Id_demande=demande, Id_sujet=sujet)

#         # Rediriger après le choix
#         return redirect('confirmation_page')  # Remplace 'confirmation_page' par le nom de la page de confirmation

#     return render(request, 'sujets/choix_sujet.html', {'sujets': sujets, 'services': services})



def choix_sujet(request):
    sujets = Sujet_stage.objects.all()
    services = Service.objects.all()

    service_id = request.GET.get('service')
    if service_id:
        sujets = sujets.filter(Id_service=service_id)

    query = request.GET.get('query')
    if query:
        sujets = sujets.filter(Q(titre__icontains=query) | Q(description__icontains=query))

    if request.method == "POST":
        sujet_id = request.POST.get('sujet_id')
        sujet = get_object_or_404(Sujet_stage, pk=sujet_id)

        candidat_id = request.session.get('candidat_id')
        if not candidat_id:
            return redirect('login_candidat')

        candidat = get_object_or_404(Candidats, Id_candidat=candidat_id)
        demandes = Demandes.objects.filter(Nom_candidat=candidat).first()

        Affectation.objects.create(Id_demande=demandes, Id_sujet=sujet)
        messages.success(request, f"Le sujet '{sujet.titre}' a été choisi et envoyé avec succès à votre encadreur.")
        # return redirect('confirmation_page')

    return render(request, 'sujets/choix_sujet.html', {'sujets': sujets, 'services': services})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Affectation, Demandes

def vue_sujets_choisis(request):
    # Récupérer toutes les affectations
    affectations = Affectation.objects.select_related('Id_sujet', 'Id_demande__Nom_candidat', 'Id_sujet__Id_service')

    if request.method == "POST":
        # Récupérer l'affectation à partir de l'ID envoyé via le formulaire
        affectation_id = request.POST.get('affectation_id')
        affectation = get_object_or_404(Affectation, pk=affectation_id)

        # Mettre à jour la table Affectation ou gérer l'affectation
        # Par exemple, mettre à jour le statut de la demande ou toute autre logique
        affectation.date_affectaion = timezone.now()  # Mettre à jour la date d'affectation
        affectation.save()

        messages.success(request, f"Le sujet '{affectation.Id_sujet.titre}' a été affecté avec succès à {affectation.Id_demande.Nom_candidat.Nom_complet}.")
        affectation.delete()

        return redirect('vue_sujets_choisis')  # Redirige après la mise à jour

    return render(request, 'sujets/vue_sujets_choisis.html', {'affectations': affectations})























# <a href="{% url 'liste_sujets_par_service' service.pk %}">
#nbghjkjh