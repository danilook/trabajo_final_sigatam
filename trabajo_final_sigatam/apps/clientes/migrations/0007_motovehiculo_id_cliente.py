# Generated by Django 3.0.7 on 2021-10-01 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_remove_motovehiculo_id_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='motovehiculo',
            name='id_cliente',
            field=models.ManyToManyField(to='clientes.Cliente'),
        ),
    ]
