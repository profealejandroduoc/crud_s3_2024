# Generated by Django 5.0.6 on 2024-06-03 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcrud', '0003_alter_mascota_tipo_alter_persona_fecha_ncto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='tipo',
            field=models.CharField(choices=[('GATO', 'Gato'), ('CONEJO', 'Conejo'), ('ANACONDA', 'Anaconda'), ('OTRO', 'Otro'), ('PERRO', 'Perro')], default='OTRO', max_length=50),
        ),
    ]
