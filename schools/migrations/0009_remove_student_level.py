# Generated by Django 3.0.3 on 2020-02-27 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0008_auto_20200227_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='level',
        ),
    ]
