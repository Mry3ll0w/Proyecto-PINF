# Generated by Django 3.2.3 on 2021-11-17 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211117_0919'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cuestionario',
        ),
        migrations.RemoveField(
            model_name='calificaciones',
            name='id',
        ),
        migrations.RemoveField(
            model_name='calificaciones',
            name='user',
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='id_usuario',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='t2_punct',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pregunta_cuestionario',
            name='id_pregunta',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]