# Generated by Django 5.0.7 on 2024-08-29 11:42

import datetime
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Affectation',
            fields=[
                ('Id_affectation', models.AutoField(primary_key=True, serialize=False)),
                ('date_affectaion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Candidats',
            fields=[
                ('Id_candidat', models.AutoField(primary_key=True, serialize=False)),
                ('Nom_complet', models.CharField(max_length=50)),
                ('universite', models.CharField(max_length=50)),
                ('niveau_academique', models.CharField(max_length=50)),
                ('specialite', models.CharField(default='TC', max_length=50)),
                ('Date_Naissance', models.DateField()),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('telephone', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(message='Le numéro de téléphone doit être un numéro national', regex='^[432]\\d{7}$')])),
                ('Date_demande', models.DateTimeField(default=django.utils.timezone.now)),
                ('cv', models.FileField(blank=True, null=True, upload_to='Documents/cv/')),
                ('lettre_motivation', models.FileField(blank=True, null=True, upload_to='Documents/lettres_motivation/')),
                ('demande', models.FileField(upload_to='Documents/demandes/')),
                ('periode', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('Id_service', models.AutoField(primary_key=True, serialize=False)),
                ('Nom_service', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('Id_utilisateur', models.AutoField(primary_key=True, serialize=False)),
                ('Nom_complet', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=191, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('RH', 'RH'), ('Encadeur', 'Encadeur'), ('User_simple', 'User_simple')], max_length=50)),
                ('Date_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Attestation',
            fields=[
                ('Id_attestation', models.AutoField(primary_key=True, serialize=False)),
                ('Date_emission', models.DateTimeField(auto_now_add=True)),
                ('chemin_attestation', models.FileField(upload_to='Attestation/%y%m%d_{stagaire}')),
                ('Id_affectation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stage_moov.affectation')),
                ('stagaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stage_moov.candidats')),
            ],
        ),
        migrations.CreateModel(
            name='Demandes',
            fields=[
                ('Id_demande', models.AutoField(primary_key=True, serialize=False)),
                ('Date_soumission', models.DateTimeField()),
                ('statut', models.CharField(max_length=50)),
                ('Id_candidat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stage_moov.candidats')),
            ],
        ),
        migrations.AddField(
            model_name='affectation',
            name='Id_demande',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stage_moov.demandes'),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('Id_document', models.AutoField(primary_key=True, serialize=False)),
                ('type_document', models.CharField(blank=True, max_length=50, null=True)),
                ('chemin_document', models.CharField(max_length=50)),
                ('Id_demande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stage_moov.demandes')),
                ('candidat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stage_moov.candidats')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('Id_evaluation', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(default='', max_length=50)),
                ('user', models.CharField(max_length=20)),
                ('files', models.FileField(upload_to='Evaluation/')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stage_moov.room')),
            ],
        ),
        migrations.CreateModel(
            name='Sujet_stage',
            fields=[
                ('Id_sujet', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('Date_creation', models.DateTimeField(auto_now_add=True)),
                ('Date_mise_a_jour', models.DateTimeField(auto_now=True)),
                ('Id_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stage_moov.service')),
            ],
        ),
        migrations.AddField(
            model_name='demandes',
            name='Id_sujet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stage_moov.sujet_stage'),
        ),
        migrations.AddField(
            model_name='affectation',
            name='Id_sujet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stage_moov.sujet_stage'),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date_envoi', models.DateTimeField(auto_now_add=True)),
                ('lu', models.BooleanField(default=False)),
                ('candidat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications_recues', to='stage_moov.candidats')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications_envoyees', to='stage_moov.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='ChoixSujet',
            fields=[
                ('Id_choix', models.AutoField(primary_key=True, serialize=False)),
                ('Date_choix', models.DateTimeField(auto_now_add=True)),
                ('affecté', models.BooleanField(default=False)),
                ('stagiaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stage_moov.candidats')),
                ('sujet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stage_moov.sujet_stage')),
                ('utilisateur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stage_moov.utilisateur')),
            ],
        ),
        migrations.AddField(
            model_name='candidats',
            name='Id_utilisateur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stage_moov.utilisateur'),
        ),
    ]
