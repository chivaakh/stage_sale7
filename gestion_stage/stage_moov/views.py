from django.shortcuts import render, redirect
from .forms import UtilisateurForm,CandidateForm,ServiceForm
from .models import Utilisateur
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Service
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import ChoixSujet,Sujet_stage
# Create your views here.
#les views pour gestions des utilisateur
def create_utilisateur(request):
    if request.method == 'POST':
        form = UtilisateurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hello')  # Replace 'success_url' with your desired redirect URL
    else:
        form = UtilisateurForm()
    
    return render(request, 'gestions_users/create_utilisateur.html', {'form': form})
def hello(request):
    return render(request,'gestions_users/hello.html',{'hello':'hello'})
def interface_principal(request):
    return render(request,'gestions_users/hello_user.html',{'home':'home'} )
def home(request):
    error_message = None  # Initialise la variable pour stocker les messages d'erreur

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if email and password:
        
            utilisateur = Utilisateur.objects.filter(Email=email).first()

            if utilisateur and utilisateur.check_password(password):
               
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

#les views pour les candidates
def create_candidate(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('#')  # Replace 'success_url' with your desired redirect URL
    else:
        form = CandidateForm()
    
    return render(request, 'gestions_candidate/create_candidate.html', {'form': form})


#les views pour la service
def service_list(request):
    query = request.GET.get('q')
    if query:
        services = Service.objects.filter(Nom_service__icontains=query)
    else:
        services = Service.objects.all()
    
    return render(request, 'service/service_list.html', {'services': services, 'query': query})

# Rest of your views...
def service_add(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'service/service_add.html', {'form': form})

def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'service/service_edit.html', {'form': form, 'service': service})

def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    return render(request, 'service/service_delete.html', {'service': service})


def sujets_par_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    sujets = Sujet_stage.objects.filter(Id_service=service)

    return render(request, 'sujets/sujets_par_service.html', {
        'service': service,
        'sujets': sujets
    })


def choisir_sujet(request, sujet_id):
    sujet = get_object_or_404(Sujet_stage, pk=sujet_id)
    candidat = request.user.candidats  # Assure-toi que l'utilisateur connecté est un candidat

    # Vérifier si le candidat a déjà fait un choix
    if ChoixSujet.objects.filter(candidat=candidat).exists():
        # Redirige ou affiche un message indiquant que le choix est déjà fait
        return redirect('sujets_par_service', service_id=sujet.Id_service.Id_service)

    choix = ChoixSujet(candidat=candidat, sujet=sujet)
    choix.save()

    return redirect('confirmation_choix')

def voir_choix_stagiaires(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    choix = ChoixSujet.objects.filter(sujet__Id_service=service)

    return render(request, 'encadrants/voir_choix_stagiaires.html', {
        'service': service,
        'choix': choix
    })

def confirmation_choix(request):
    return render(request, 'sujets/confirmation_choix.html', {'message': 'Votre choix a été enregistré.'})



def liste_sujets(request):
    sujets = Sujet_stage.objects.all()
    return render(request, 'Sujet/liste_sujets.html', {'sujets': sujets})

