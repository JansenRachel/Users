# Generated by Django 2.2 on 2021-08-03 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0002_auto_20210803_1704'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
    ]