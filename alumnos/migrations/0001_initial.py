# Generated by Django 4.0.3 on 2022-03-19 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=40)),
                ('dni', models.IntegerField()),
                ('clave', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=50)),
                ('tutor', models.CharField(max_length=50)),
                ('tutor_telefono', models.IntegerField()),
                ('tutor_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
