# Generated by Django 4.2.1 on 2023-05-13 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_pasillo_seccion_alter_detalle_bodega_cantidadprod_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalle_bodega',
            name='lugarProd',
        ),
    ]
