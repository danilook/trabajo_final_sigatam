# Generated by Django 3.0.7 on 2020-09-15 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=250)),
                ('dni', models.IntegerField()),
                ('rol', models.CharField(max_length=200)),
                ('fecha_alta', models.DateField()),
                ('reputacion', models.IntegerField()),
            ],
        ),
    ]
