from django.db import models
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.base import ContentFile
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from datetime import datetime


class Utilisateur(models.Model):
    
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('RH', 'RH'),
        ('Encadreur', 'Encadreur'),
        ('User_simple', 'User_simple'),
    ]
    Id_utilisateur = models.AutoField(primary_key=True)
    Nom_complet = models.CharField(max_length=50)
    
    Email = models.EmailField(max_length=191, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField( choices=ROLE_CHOICES, max_length=50)
    Date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Nom_complet
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    

class Candidats(models.Model):
    Id_candidat = models.AutoField(primary_key=True)
    Id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True, blank=True)
    Nom_complet = models.CharField(max_length=50)
    universite = models.CharField(max_length=50)
    niveau_academique = models.CharField(max_length=50)
    specialite= models.CharField(max_length=50, default='TC')
    Date_Naissance = models.DateField()
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    telephone = models.CharField(max_length=8, validators=[RegexValidator(regex=r'^[432]\d{7}$', message="Le numéro de téléphone doit être un numéro national")])
    Date_demande = models.DateTimeField(default=timezone.now)
    cv = models.FileField(upload_to='Documents/cv/',null=True,blank=True)
    lettre_motivation = models.FileField(upload_to='Documents/lettres_motivation/',null=True,blank=True)
    demande = models.FileField(upload_to='Documents/demandes/', null=False,blank=False)
    periode = models.CharField(max_length=50)

    def __str__(self):
        return self.Nom_complet
    


class Service(models.Model):
    Id_service = models.AutoField(primary_key=True)
    Nom_service = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)



    def __str__(self):
        return self.Nom_service

class Sujet_stage(models.Model):
    Id_sujet = models.AutoField(primary_key=True)
    Id_service = models.ForeignKey(Service, on_delete=models.CASCADE)
    titre = models.CharField(max_length=50)
    description = models.TextField()  # Assurez-vous que c'est bien en minuscules
    Date_creation = models.DateTimeField(auto_now_add=True)
    Date_mise_a_jour = models.DateTimeField(auto_now=True)





class Demandes(models.Model):
    Id_demande = models.AutoField(primary_key=True)
    Nom_candidat = models.ForeignKey(Candidats, on_delete=models.CASCADE)
    Date_soumission = models.DateTimeField()
    statut = models.CharField(max_length=50)

    def __str__(self):
        return str(self.Id_demande)

class Document(models.Model):
    Id_document = models.AutoField(primary_key=True)
    candidat = models.ForeignKey(Candidats, on_delete=models.CASCADE)
    Id_demande = models.ForeignKey(Demandes, on_delete=models.CASCADE)
    type_document = models.CharField(max_length=50, null=True, blank=True)
    chemin_document = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.candidat.Nom_complet}"

class Affectation(models.Model):
    Id_affectation = models.AutoField(primary_key=True)
    Id_demande = models.ForeignKey(Demandes, on_delete=models.CASCADE)
    Id_sujet = models.ForeignKey(Sujet_stage, on_delete=models.CASCADE)
    date_affectaion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.Id_affectation)

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)  

    def __str__(self):
        return self.name

class Evaluation(models.Model):
    Id_evaluation = models.AutoField(primary_key=True)
    content = models.CharField(max_length=50, default='') 
    user = models.CharField(max_length=20, null=False, blank=False) 
    files=models.FileField(upload_to='Evaluation/')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f'Evaluation {self.Id_evaluation} by {self.user}'
class Attestation(models.Model):
    Id_attestation = models.AutoField(primary_key=True)
    Id_affectation = models.ForeignKey(Affectation, on_delete=models.CASCADE)
    stagaire = models.ForeignKey(Candidats, on_delete=models.CASCADE)
    Date_emission = models.DateTimeField(auto_now_add=True)
    chemin_attestation = models.FileField(upload_to='Attestation/%y%m%d_{stagaire}')

    def __str__(self):
        return str(self.Id_attestation)

class Notification(models.Model):
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='notifications_envoyees')
    candidat = models.ForeignKey(Candidats, on_delete=models.CASCADE, related_name='notifications_recues')

    
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Candidats)
def create_demande(sender, instance, created, **kwargs):
    if created:
        Demandes.objects.create(
            Nom_candidat=instance,
            Date_soumission=instance.Date_demande,
            statut="En attente"
        )


