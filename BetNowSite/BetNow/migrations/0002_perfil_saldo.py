# Generated by Django 4.2 on 2023-06-09 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BetNow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='saldo',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]