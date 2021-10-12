# Generated by Django 3.0.7 on 2021-10-08 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0007_proveedor_estado'),
        ('repuestos', '0003_compra_id_repuesto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repuesto',
            name='categoria',
        ),
        migrations.AddField(
            model_name='repuesto',
            name='id_categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='proveedores.categoria'),
        ),
    ]
