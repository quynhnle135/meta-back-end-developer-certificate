# Generated by Django 4.1.4 on 2023-06-27 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_course_menuitems_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitems',
            old_name='name',
            new_name='itemname',
        ),
    ]
