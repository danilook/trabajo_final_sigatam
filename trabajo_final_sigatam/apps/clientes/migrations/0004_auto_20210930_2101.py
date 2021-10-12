# Generated by Django 3.0.7 on 2021-10-01 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_cliente_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='motovehiculo',
            name='cliente_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='motovehiculo',
            name='color',
            field=models.CharField(default='', max_length=100, verbose_name='Color del motovehiculo'),
        ),
    ]