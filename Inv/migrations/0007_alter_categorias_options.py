# Generated by Django 5.0.6 on 2024-06-24 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inv', '0006_alter_producto_options_producto_codigo_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorias',
            options={'permissions': [('view_categoria', 'Can view categorias')], 'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
    ]
