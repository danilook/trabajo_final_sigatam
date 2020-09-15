# Generated by Django 3.0.7 on 2020-09-15 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=220)),
                ('apellido', models.CharField(max_length=220)),
                ('dni', models.IntegerField()),
                ('direccion', models.CharField(max_length=220)),
                ('correo', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
            ],
        ),
    ]