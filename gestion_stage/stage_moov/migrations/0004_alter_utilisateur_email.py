# Generated by Django 5.0.7 on 2024-08-19 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage_moov', '0003_alter_utilisateur_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='Email',
            field=models.EmailField(max_length=70, unique=True),
        ),
    ]
