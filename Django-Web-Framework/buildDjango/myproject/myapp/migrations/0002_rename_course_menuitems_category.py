# Generated by Django 4.1.4 on 2023-06-27 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitems',
            old_name='course',
            new_name='category',
        ),
    ]