# Generated by Django 5.1.1 on 2024-09-19 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='version',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
