# Generated by Django 3.2.13 on 2022-06-09 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('descriptif', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
