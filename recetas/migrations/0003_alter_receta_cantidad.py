# Generated by Django 4.2.16 on 2024-12-04 03:46

from django.db import migrations, models
import recetas.validators


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0002_rename_id_medicamento_receta_medicamento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='cantidad',
            field=models.IntegerField(validators=[recetas.validators.validar_positivos]),
        ),
    ]
