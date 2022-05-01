# Generated by Django 3.0.7 on 2021-10-25 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0002_tipoturno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turno',
            name='tipo_turno',
        ),
        migrations.AddField(
            model_name='turno',
            name='id_tipoTurno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='turnos.tipoTurno'),
        ),
    ]