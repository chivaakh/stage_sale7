from django import forms
from .models import Utilisateur,Candidats,Service
from django.contrib.auth.hashers import make_password
from .models import Sujet_stage 
from .models import Notification
from django.contrib.auth.models import User
from .models import Notification



class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['Nom_complet', 'Email', 'password', 'role']

        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
       
        utilisateur = super().save(commit=False)
        utilisateur.password = make_password(self.cleaned_data['password'])
        if commit:
            utilisateur.save()
        return utilisateur

#formulaire pour la candidate
class AdminCandidatForm(forms.ModelForm):
    class Meta:
        model = Candidats
        fields = ['Id_utilisateur', 'Nom_complet', 'universite', 'niveau_academique','specialite','Date_Naissance','email', 'password','telephone','cv','lettre_motivation','demande','periode']  

        
class CandidatForm(forms.ModelForm):
    class Meta:
        model = Candidats
        fields = ['Nom_complet', 'universite', 'niveau_academique', 'specialite', 'Date_Naissance', 'email', 'password', 'telephone', 'cv', 'lettre_motivation', 'demande', 'periode']
    
    def save(self, commit=True):
        candidate = super().save(commit=False)
        
        if commit:
            candidate.save()

        return candidate



#formulaire pour ajouter une service
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['Nom_service', 'description']
    
    def save(self, commit=True):
        
        service = super().save(commit=False)
        
        if commit:
            service.save()
        return service




class SujetStageForm(forms.ModelForm):
    class Meta:
        model = Sujet_stage
        fields = ['titre', 'Description', 'Id_service']  # Inclure le service ici



        fields = ['titre', 'description']
