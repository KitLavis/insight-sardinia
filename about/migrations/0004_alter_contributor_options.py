# Generated by Django 4.2.9 on 2024-01-15 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_alter_contributor_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contributor',
            options={'ordering': ['name']},
        ),
    ]
