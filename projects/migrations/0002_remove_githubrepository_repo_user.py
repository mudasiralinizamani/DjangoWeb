# Generated by Django 3.0.8 on 2020-11-01 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='githubrepository',
            name='repo_user',
        ),
    ]
