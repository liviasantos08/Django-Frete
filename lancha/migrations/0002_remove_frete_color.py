# Generated by Django 4.0.3 on 2022-05-14 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancha', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frete',
            name='color',
        ),
    ]
