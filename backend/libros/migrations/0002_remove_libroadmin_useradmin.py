# Generated by Django 5.0 on 2024-05-26 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libroadmin',
            name='userAdmin',
        ),
    ]