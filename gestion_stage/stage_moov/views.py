from django.shortcuts import render, redirect
from .forms import UtilisateurForm,CandidateForm,ServiceForm
from .models import Utilisateur
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Service,Utilisateur,Candidats,Demandes
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Notification
from .forms import CandidatForm
from django.db.models import Q
from .forms import SujetStageForm
from .models import Sujet_stage



# Create your views here.
#les views pour gestions des utilisateur
def create_utilisateur(request):
    if request.method == 'POST':
        form = UtilisateurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('interface_principal')  
    else:
        form = UtilisateurForm()
    
    return render(request, 'gestions_users/create_utilisateur.html', {'form': form})

def hello(request):
    return render(request,'gestions_users/hello.html',{'hello':'hello'})
#fonction pour la login
def login(request):
    error_message = None  # Initialise la variable pour stocker les messages d'erreur

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if email and password:
        
            utilisateur = Utilisateur.objects.filter(Email=email).first()
            if utilisateur and utilisateur.check_password(password):
                if utilisateur and utilisateur.role.strip().lower() == 'admin':
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
            return redirect('#')  # Replace 'success_url' with your desired redirect URL
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

def notifications_view(request):
    notifications = Notification.objects.filter(utilisateur=request.user, statut="non lu")
    return render(request, 'notifications.html', {'notifications': notifications})



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

