# Generated by Django 4.2.2 on 2023-06-27 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_drinks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_item', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_category_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Drinks',
        ),
        migrations.DeleteModel(
            name='Menuitems',
        ),
        migrations.AddField(
            model_name='menu',
            name='category_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='myapp.menucategory'),
        ),
    ]
