# Generated by Django 5.0.7 on 2024-08-12 15:25

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
            name='Service',
            fields=[
                ('Id_service', models.AutoField(primary_key=True, serialize=False)),
                ('Nom_service', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
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
            name='Sujet_stage',
            fields=[
                ('Id_sujet', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=50)),
                ('Description', models.TextField()),
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
            name='Utilisateur',
            fields=[
                ('Id_utilisateur', models.AutoField(primary_key=True, serialize=False)),
                ('Nom_complet', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('Date_creation', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'indexes': [models.Index(fields=['Email'], name='stage_moov__Email_d4251a_idx')],
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('Id_notification', models.AutoField(primary_key=True, serialize=False)),
                ('Message', models.TextField(max_length=50)),
                ('Date_notification', models.DateTimeField(auto_now_add=True)),
                ('statut', models.CharField(max_length=50)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stage_moov.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('Id_evaluation', models.AutoField(primary_key=True, serialize=False)),
                ('commentaire', models.TextField()),
                ('Note_performance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_evaluation', models.DateTimeField(auto_now=True)),
                ('Id_affectation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stage_moov.affectation')),
                ('Id_candidat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stage_moov.candidats')),
                ('Id_utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stage_moov.utilisateur')),
            ],
        ),
        migrations.AddField(
            model_name='candidats',
            name='Id_utilisateur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stage_moov.utilisateur'),
        ),
    ]
