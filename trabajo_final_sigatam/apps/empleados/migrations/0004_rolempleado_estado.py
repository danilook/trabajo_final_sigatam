# Generated by Django 3.0.7 on 2022-05-03 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0003_empleado_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='rolempleado',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]
