# Generated by Django 4.0.3 on 2022-06-16 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_film'),
    ]

    operations = [
        migrations.CreateModel(
            name='Realisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='film',
            name='annee',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='film',
            name='realisateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.realisateur'),
        ),
    ]
