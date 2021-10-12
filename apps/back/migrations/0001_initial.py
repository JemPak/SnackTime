# Generated by Django 3.2.7 on 2021-10-06 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False, verbose_name='id cliente')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('nit', models.IntegerField(verbose_name='identificacion')),
                ('direc', models.CharField(blank=True, max_length=200, null=True, verbose_name='direccion')),
                ('ciudad', models.CharField(max_length=80, verbose_name='ciudad')),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.IntegerField(verbose_name='telefono')),
            ],
        ),
    ]