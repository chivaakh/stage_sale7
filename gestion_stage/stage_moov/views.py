from django.shortcuts import render, redirect,get_object_or_404
from .forms import UtilisateurForm,CandidateForm,ServiceForm,SujetStageForm
from .models import *
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

# Create your views here.
#les views pour gestions des utilisateur

from django.shortcuts import render, get_object_or_404, redirect
from .models import Candidats, Notification

def liste_candidats(request):
    candidats = Candidats.objects.all()
    return render(request, 'utilisateur/liste_candidats.html', {'candidats': candidats})

logger = logging.getLogger(__name__)

def envoyer_message(request, candidat_id):
    candidat = get_object_or_404(Candidats, pk=candidat_id)
    if request.method == 'POST':
        message = request.POST.get('message')
        
        utilisateur_django = request.user
        logger.debug(f'Utilisateur Django connecté : {utilisateur_django.email}')
        
        # Essayer de récupérer l'utilisateur personnalisé basé sur l'email
        try:
            utilisateur = Utilisateur.objects.get(Email=utilisateur_django.email)
            logger.debug(f'Utilisateur trouvé : {utilisateur.Nom_complet}')
        except Utilisateur.DoesNotExist:
            logger.error(f'Utilisateur non trouvé pour l\'email : {utilisateur_django.email}')
            return render(request, 'sidebar/error.html', {'error_message': "Utilisateur non trouvé."})

        # Créer la notification
        notification = Notification.objects.create(
            message=message,
            utilisateur=utilisateur,
            candidat=candidat
        )
        notification.save()
        
         

        return redirect('liste_messages')
     
    return render(request, 'utilisateur/envoyer_message.html', {'candidat': candidat})
    

def liste_messages(request):
    
    notifications = Notification.objects.all()
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
        return redirect('interface_principal')

    return render(request, 'gestions_users/home.html')
#fonction pour la login
def login(request):
    error_message = None  # Initialise la variable pour stocker les messages d'erreur

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email and password:
        
            utilisateur = Utilisateur.objects.filter(Email=email).first()
            if utilisateur and utilisateur.check_password(password):
                if utilisateur and utilisateur.role == 'Admin':
                    return redirect('interface_principal') 
                elif utilisateur and utilisateur.role == 'RH':
                     return redirect('gestion_demandes') 
                else:
                     return redirect('hello') 
                
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


#les views pour les creet de candidate
def create_candidate(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Candidats/confirmation.html')  # Replace 'success_url' with your desired redirect URL
    else:
        form = CandidateForm()
    
    return render(request, 'Candidats/code.html', {'form': form})

#les fonction CRUD pour gestions les utilisateurs
def interface_principal(request):
    utilisateur=Utilisateur.objects.all()
    return render(request,'gestions_users/Interface_principale.html',{'utilisateur': utilisateur} )
def deletuser(request, id_user):
    utilisateur = Utilisateur.objects.filter(Id_utilisateur=id_user).first()  
    if utilisateur: 
        utilisateur.delete()  
    return redirect('interface_principal') 

#RD pour la candidate
def show_candidate(request):
    candidate=Candidats.objects.all()
    return render(request,'Candidats/show_candidat.html',{'candidate':candidate})

def delete_candidate(request,id_candidate):
    candidate=Candidats.objects.filter(Id_candidat=id_candidate).first()
    if candidate:
        candidate.delete()
    return redirect('show_candidat')

#pour gestion des demandes
def gestion_demandes(request):
    if not request.user.is_authenticated:
        return redirect('login')
    demandes = Demandes.objects.all()
    return render(request, 'gestion_demande/gestion_demandes.html',{'demandes': demandes})
#les views pour accepter
def accepter_demande(request, demande_id):
   demande = Demandes.objects.filter(Id_demande=demande_id).first()
   demande.statut = 'accepter'
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
    query = request.GET.get('q')
    if query:
        services = Service.objects.filter(Nom_service__icontains=query)
    else:
        services = Service.objects.all()
    
    return render(request, 'Service/service_list.html', {'services': services, 'query': query})

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
            return redirect('confirmation')  # Redirigez vers une page de confirmation ou autre
    else:
        form = CandidatForm()
    return render(request, 'Candidats/candidats.html', {'form': form})

def confirmation(request):
    return render(request, 'Candidats/confirmation.html')

def form_candidat(request):
    return render(request, 'Candidats/code.html')


    return render(request, 'Notifications/notifications.html', {'notifications': notifications})
def create_candidate(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            candidate = form.save()
            # Créer une notification pour l'utilisateur
            Notification.objects.create(
                utilisateur=request.user,
                message="Un nouveau candidat a été créé."
            )
            return redirect('Candidats/confirmation.html')
    else:
        form = CandidateForm()

    return render(request, 'Candidats/code.html', {'form': form})



# Liste des sujets
def liste_sujets(request):
    query = request.GET.get('query', '')
    if query:
        sujets = Sujet_stage.objects.filter(
            Q(titre__icontains=query) | Q(Description__icontains=query)
        )
    else:
        sujets = Sujet_stage.objects.all()
    context = {
        'sujets': sujets,
    }
    return render(request, 'Sujets/liste.html', context)


# Ajouter un sujet
def ajouter_sujet(request):
    if request.method == "POST":
        form = SujetStageForm(request.POST)
        if form.is_valid():
            sujet = form.save(commit=False)
            sujet.save()
            return redirect('liste_sujets')
    else:
        form = SujetStageForm()
    return render(request, 'Sujets/ajouter.html', {'form': form})

# Modifier un sujet
def modifier_sujet(request, pk):
    sujet = get_object_or_404(Sujet_stage, pk=pk)
    if request.method == "POST":
        form = SujetStageForm(request.POST, instance=sujet)
        if form.is_valid():
            form.save()
            return redirect('liste_sujets')
    else:
        form = SujetStageForm(instance=sujet)
    return render(request, 'Sujets/modifier.html', {'form': form})

# Supprimer un sujet
def supprimer_sujet(request, pk):
    sujet = get_object_or_404(Sujet_stage, pk=pk)
    sujet.delete()
    return redirect('liste_sujets')

def liste_sujets_par_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    sujets = Sujet_stage.objects.filter(Id_service=service)
    context = {
        'service': service,
        'sujets': sujets,
    }
    return render(request, 'Sujets/liste_par_service.html', context)

def homepage(request):
    return render(request, 'first/code.html')

#les view pour evaluation
def start_chat(request):
    return render(request, 'evaluation/lancer_chat.html')

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
    message = request.POST['message']
    username = request.POST['username']
    room_name= request.POST['room_id']

    new_message = Evaluation.objects.create(content= message , user = username , room = room_name)
    new_message.save()
    return HttpResponse('Message envoyé avec succès')

def getMessages(request , room):
    room_details = Room.objects.get(name=room)
    messages = Evaluation.objects.filter(room = room_details.id).order_by('date')
    return JsonResponse({"messages" :list(messages.values())})


#dfghjkjhg