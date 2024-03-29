# Generated by Django 3.1.2 on 2020-11-09 12:58

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_auto_20201108_0925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='student',
            new_name='grade',
        ),
        migrations.AlterField(
            model_name='category',
            name='date',
            field=models.CharField(default='15 November 2020', max_length=255),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
