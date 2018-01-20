# Generated by Django 2.0.1 on 2018-01-20 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adopciones', '0001_initial'),
        ('mascotas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacunas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='mascotas',
            name='persona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adopciones.Personas'),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='vacuna',
            field=models.ManyToManyField(to='mascotas.Vacunas'),
        ),
    ]
