# Generated by Django 3.0.7 on 2021-10-25 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tipoTurno',
            fields=[
                ('id_tipoTurno', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200, verbose_name='Tipo de turno')),
            ],
        ),
    ]