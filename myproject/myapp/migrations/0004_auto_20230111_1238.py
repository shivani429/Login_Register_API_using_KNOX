# Generated by Django 3.2.16 on 2023-01-11 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20230111_1236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='model',
            old_name='firstname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='model',
            name='lastname',
        ),
    ]
