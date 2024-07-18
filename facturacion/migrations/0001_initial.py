# Generated by Django 5.0.6 on 2024-06-28 17:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='estado')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha-creacion')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='fecha-modificacion')),
                ('usuario_modificacion', models.IntegerField(blank=True, null=True)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('celular', models.CharField(blank=True, max_length=10, null=True)),
                ('tipo', models.CharField(choices=[('NATURAL', 'NATURAL'), ('JURIDICA', 'JURIDICA')], default='NATURAL', max_length=10)),
                ('usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
