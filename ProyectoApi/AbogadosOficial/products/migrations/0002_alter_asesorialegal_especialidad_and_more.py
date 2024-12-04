# Generated by Django 5.1.3 on 2024-11-27 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asesorialegal',
            name='especialidad',
            field=models.CharField(db_column='especialidad', max_length=255),
        ),
        migrations.RenameField(
            model_name='asesorialegal',
            old_name='especialidad',
            new_name='_especialidad',
        ),
        migrations.AlterField(
            model_name='asesorialegal',
            name='num_asesorias',
            field=models.IntegerField(db_column='num_asesorias'),
        ),
        migrations.RenameField(
            model_name='asesorialegal',
            old_name='num_asesorias',
            new_name='_num_asesorias',
        ),
        migrations.AlterField(
            model_name='divorcio',
            name='duracion_estimada',
            field=models.DecimalField(db_column='duracion_estimada', decimal_places=2, max_digits=5),
        ),
        migrations.RenameField(
            model_name='divorcio',
            old_name='duracion_estimada',
            new_name='_duracion_estimada',
        ),
        migrations.AlterField(
            model_name='divorcio',
            name='num_divorcios',
            field=models.IntegerField(db_column='num_divorcios'),
        ),
        migrations.RenameField(
            model_name='divorcio',
            old_name='num_divorcios',
            new_name='_num_divorcios',
        ),
        migrations.AlterField(
            model_name='serviciolegal',
            name='costo',
            field=models.DecimalField(db_column='costo', decimal_places=2, max_digits=10),
        ),
        migrations.RenameField(
            model_name='serviciolegal',
            old_name='costo',
            new_name='_costo',
        ),
        migrations.AlterField(
            model_name='serviciolegal',
            name='descripcion',
            field=models.CharField(db_column='descripcion', max_length=255),
        ),
        migrations.RenameField(
            model_name='serviciolegal',
            old_name='descripcion',
            new_name='_descripcion',
        ),
        migrations.AlterField(
            model_name='serviciolegal',
            name='nombre_servicio',
            field=models.CharField(db_column='nombre_servicio', max_length=255, unique=True),
        ),
        migrations.RenameField(
            model_name='serviciolegal',
            old_name='nombre_servicio',
            new_name='_nombre_servicio',
        ),
    ]
