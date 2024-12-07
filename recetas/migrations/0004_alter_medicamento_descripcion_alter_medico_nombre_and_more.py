# Generated by Django 4.2.17 on 2024-12-05 00:05

from django.db import migrations, models
import recetas.validators


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0003_alter_receta_cantidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='descripcion',
            field=models.CharField(max_length=100, validators=[recetas.validators.validar_nulos]),
        ),
        migrations.AlterField(
            model_name='medico',
            name='nombre',
            field=models.CharField(max_length=100, validators=[recetas.validators.validar_nulos]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nombre',
            field=models.CharField(max_length=35, validators=[recetas.validators.validar_nulos]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='paterno',
            field=models.CharField(max_length=35, validators=[recetas.validators.validar_nulos]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(max_length=1, validators=[recetas.validators.validar_sexo]),
        ),
        migrations.AlterField(
            model_name='receta',
            name='cantidad',
            field=models.IntegerField(validators=[recetas.validators.validar_positivos, recetas.validators.validar_maximo]),
        ),
        migrations.AlterField(
            model_name='receta',
            name='diagnostico',
            field=models.TextField(validators=[recetas.validators.validar_nulos]),
        ),
        migrations.AlterField(
            model_name='receta',
            name='dosis',
            field=models.TextField(validators=[recetas.validators.validar_nulos]),
        ),
    ]
