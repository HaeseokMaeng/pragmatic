# Generated by Django 3.1.4 on 2020-12-29 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0002_auto_20201228_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_at',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]