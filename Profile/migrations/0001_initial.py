# Generated by Django 3.0.2 on 2020-02-23 19:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CiudadModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('delete', models.BooleanField(default=False)),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Ciudad',
            },
        ),
        migrations.CreateModel(
            name='EstadoCivilModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('delete', models.BooleanField(default=False)),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'EstadoCivil',
            },
        ),
        migrations.CreateModel(
            name='EstadoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('delete', models.BooleanField(default=False)),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Estado',
            },
        ),
        migrations.CreateModel(
            name='GeneroModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('delete', models.BooleanField(default=False)),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Genero',
            },
        ),
        migrations.CreateModel(
            name='OcupacionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('delete', models.BooleanField(default=False)),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Ocupacion',
            },
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('apPat', models.CharField(max_length=254)),
                ('apMat', models.CharField(max_length=254)),
                ('edad', models.IntegerField()),
                ('delete', models.BooleanField(default=False)),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.CiudadModel')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.EstadoModel')),
                ('estadoCivil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.EstadoCivilModel')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.GeneroModel')),
                ('ocupacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.OcupacionModel')),
            ],
            options={
                'db_table': 'Profile',
            },
        ),
    ]
