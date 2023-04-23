# Generated by Django 4.2 on 2023-04-23 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BetNow', '0004_remove_perfil_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='celular',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='numero_documento',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
