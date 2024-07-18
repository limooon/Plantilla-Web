# Generated by Django 5.0.6 on 2024-06-20 18:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inv', '0005_alter_unidadmedida_options_unidadmedida_descripcion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'verbose_name_plural': 'Productos'},
        ),
        migrations.AddField(
            model_name='producto',
            name='codigo',
            field=models.CharField(default=None, max_length=20, unique=True, verbose_name='codigo'),
        ),
        migrations.AddField(
            model_name='producto',
            name='codigo_barra',
            field=models.CharField(default=None, max_length=50, verbose_name='codigo barra'),
        ),
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(default=None, max_length=200, verbose_name='descripcion'),
        ),
        migrations.AddField(
            model_name='producto',
            name='existencia',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='producto',
            name='marca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Inv.marca'),
        ),
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='producto',
            name='subcategoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Inv.subcategorias'),
        ),
        migrations.AddField(
            model_name='producto',
            name='ultima_compra',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='unidad_medida',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Inv.unidadmedida'),
        ),
        migrations.AlterUniqueTogether(
            name='producto',
            unique_together={('codigo', 'codigo_barra')},
        ),
    ]
