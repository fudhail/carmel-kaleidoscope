# Generated by Django 3.1.2 on 2020-10-28 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20201028_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='student',
        ),
    ]
