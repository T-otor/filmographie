# Generated by Django 4.0.3 on 2022-06-16 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_alter_film_acteur_principal_alter_film_annee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='avis',
            field=models.CharField(default='defaut', max_length=100000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='film',
            name='pseudo',
            field=models.CharField(default='defaut', max_length=50),
            preserve_default=False,
        ),
    ]
