# Generated by Django 5.0.6 on 2024-06-18 15:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcrud', '0009_alter_carrito_persona_alter_carrito_usuario_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='tipo',
            field=models.CharField(choices=[('ANACONDA', 'Anaconda'), ('GATO', 'Gato'), ('PERRO', 'Perro'), ('CONEJO', 'Conejo'), ('OTRO', 'Otro')], default='OTRO', max_length=50),
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=9)),
                ('direccion', models.CharField(max_length=250)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]