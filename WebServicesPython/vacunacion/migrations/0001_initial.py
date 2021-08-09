# Generated by Django 3.2.6 on 2021-08-09 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cantones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canton', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='centro_vacunacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centro_vacunacion', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=60)),
                ('canton', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='centro_vacunacion', to='vacunacion.cantones')),
            ],
        ),
        migrations.CreateModel(
            name='provincias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provincia', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='parroquias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parroquia', models.CharField(max_length=85)),
                ('canton', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='parroquias', to='vacunacion.cantones')),
            ],
        ),
        migrations.CreateModel(
            name='ciudadanos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre1', models.CharField(max_length=20)),
                ('nombre2', models.CharField(max_length=20)),
                ('apellido1', models.CharField(max_length=20)),
                ('apellido2', models.CharField(max_length=20)),
                ('cedula', models.CharField(max_length=10)),
                ('primeraDosis', models.CharField(max_length=40)),
                ('segundaDosis', models.CharField(max_length=40)),
                ('canton', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ciudadanos', to='vacunacion.cantones')),
                ('centroVacunacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ciudadanos', to='vacunacion.centro_vacunacion')),
                ('parroquia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ciudadanos', to='vacunacion.parroquias')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ciudadanos', to='vacunacion.provincias')),
            ],
        ),
        migrations.AddField(
            model_name='cantones',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cantones', to='vacunacion.provincias'),
        ),
    ]