# Generated by Django 4.2.9 on 2024-01-15 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='slug',
            field=models.CharField(default='empty', max_length=200),
        ),
    ]