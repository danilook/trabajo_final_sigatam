# Generated by Django 3.0.7 on 2021-10-08 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0007_proveedor_estado'),
        ('repuestos', '0004_auto_20211007_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='id_proveedor',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='proveedores.Proveedor'),
        ),
    ]
