# Generated by Django 3.1.2 on 2020-11-10 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_auto_20201110_1146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pdf',
            new_name='video_or_not',
        ),
        migrations.RemoveField(
            model_name='post',
            name='video',
        ),
    ]
