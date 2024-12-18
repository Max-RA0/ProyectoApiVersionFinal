# Generated by Django 5.1.3 on 2024-11-18 04:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServicioLegal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_servicio', models.CharField(max_length=255, unique=True)),
                ('descripcion', models.CharField(max_length=255)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AsesoriaLegal',
            fields=[
                ('serviciolegal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.serviciolegal')),
                ('num_asesorias', models.IntegerField()),
                ('especialidad', models.CharField(max_length=255)),
            ],
            bases=('products.serviciolegal',),
        ),
        migrations.CreateModel(
            name='Divorcio',
            fields=[
                ('serviciolegal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.serviciolegal')),
                ('num_divorcios', models.IntegerField()),
                ('duracion_estimada', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            bases=('products.serviciolegal',),
        ),
    ]
