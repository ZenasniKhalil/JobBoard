# Generated by Django 4.1.3 on 2022-12-15 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_requirements'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Requirements',
        ),
    ]