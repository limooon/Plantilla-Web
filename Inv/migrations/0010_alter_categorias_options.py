# Generated by Django 5.0.6 on 2024-06-24 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inv', '0009_alter_categorias_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorias',
            options={'permissions': [('view_categoria', 'Can view categorias'), ('add_categoria', 'Can add categoria'), ('change_Categoria', 'Puede cambiar MiModelo'), ('delete_categoria', 'Can delete categoria')], 'verbose_name': 'Categoria'},
        ),
    ]
