# Generated by Django 3.0.7 on 2021-10-05 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0006_auto_20211002_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]