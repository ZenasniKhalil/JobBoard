# Generated by Django 4.1.3 on 2022-12-15 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('require', models.CharField(max_length=100)),
                ('job_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.jobmodel')),
            ],
        ),
    ]