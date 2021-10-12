# Generated by Django 3.0.7 on 2021-10-08 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0007_proveedor_estado'),
        ('repuestos', '0005_compra_id_proveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='id_proveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='proveedores.Proveedor'),
        ),
        migrations.RemoveField(
            model_name='compra',
            name='id_repuesto',
        ),
        migrations.AddField(
            model_name='compra',
            name='id_repuesto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='repuestos.Repuesto'),
        ),
    ]
