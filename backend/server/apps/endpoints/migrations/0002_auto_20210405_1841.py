# Generated by Django 3.1.7 on 2021-04-05 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endpoint',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
