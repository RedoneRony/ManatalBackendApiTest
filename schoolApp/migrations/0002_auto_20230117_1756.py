# Generated by Django 3.2.16 on 2023-01-17 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='_id',
            new_name='id',
        ),
    ]
