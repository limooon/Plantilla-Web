# Generated by Django 5.0.6 on 2024-06-25 20:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inv', '0012_alter_categorias_options'),
        ('cmp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ComprasEncabezado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='estado')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha-creacion')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='fecha-modificacion')),
                ('usuario_modificacion', models.IntegerField(blank=True, null=True)),
                ('fecha_compra', models.DateField(blank=True, null=True)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('no_factura', models.CharField(max_length=100)),
                ('fecha_factura', models.DateField()),
                ('sub_total', models.FloatField(default=0)),
                ('descuento', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('provedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmp.provedor')),
                ('usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Compra Encabezado',
                'verbose_name_plural': 'Compras Encabezados',
            },
        ),
        migrations.CreateModel(
            name='ComprasDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='estado')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha-creacion')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='fecha-modificacion')),
                ('usuario_modificacion', models.IntegerField(blank=True, null=True)),
                ('cantidad', models.BigIntegerField(default=0)),
                ('precio_prv', models.FloatField(default=0)),
                ('sub_total', models.FloatField(default=0)),
                ('descuento', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('costo', models.FloatField(default=0)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inv.producto')),
                ('usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmp.comprasencabezado')),
            ],
            options={
                'verbose_name': 'Compra Detalle',
                'verbose_name_plural': 'Compras Detalles',
            },
        ),
    ]
