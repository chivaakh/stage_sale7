# Generated by Django 5.0.7 on 2024-08-26 10:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage_moov', '0002_rename_description_sujet_stage_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoixSujet',
            fields=[
                ('Id_choix', models.AutoField(primary_key=True, serialize=False)),
                ('Date_choix', models.DateTimeField(auto_now_add=True)),
                ('affecté', models.BooleanField(default=False)),
                ('stagiaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sujet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stage_moov.sujet_stage')),
            ],
        ),
    ]
