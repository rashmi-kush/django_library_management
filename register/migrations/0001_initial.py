# Generated by Django 4.0.2 on 2022-09-15 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registermod',
            fields=[
                ('userid', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=8)),
            ],
        ),
    ]