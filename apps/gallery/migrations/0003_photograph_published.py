# Generated by Django 4.2 on 2023-04-27 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_photograph_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='photograph',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]