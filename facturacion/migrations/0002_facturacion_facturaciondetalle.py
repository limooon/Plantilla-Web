# Generated by Django 5.0.6 on 2024-06-28 21:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inv', '0012_alter_categorias_options'),
        ('facturacion', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Facturacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='estado')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha-creacion')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='fecha-modificacion')),
                ('usuario_modificacion', models.IntegerField(blank=True, null=True)),
                ('fecha_total', models.DateField()),
                ('descuento', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.cliente')),
                ('usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Encabezado de Factura',
                'verbose_name_plural': 'Encabezado de Facturas',
            },
        ),
        migrations.CreateModel(
            name='FacturacionDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='estado')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha-creacion')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='fecha-modificacion')),
                ('usuario_modificacion', models.IntegerField(blank=True, null=True)),
                ('cantidad', models.BigIntegerField(default=0)),
                ('precio', models.FloatField(default=0)),
                ('sub_total', models.FloatField(default=0)),
                ('dscuento', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.facturacion')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inv.producto')),
                ('usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Detalle de Factura',
                'verbose_name_plural': 'Detalle de Facturas',
            },
        ),
    ]
