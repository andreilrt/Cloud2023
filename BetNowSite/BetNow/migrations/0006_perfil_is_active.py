# Generated by Django 4.2 on 2023-04-23 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BetNow', '0005_alter_perfil_celular_alter_perfil_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
