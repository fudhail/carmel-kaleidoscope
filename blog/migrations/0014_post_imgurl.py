# Generated by Django 3.1.2 on 2020-10-26 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20201025_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imgurl',
            field=models.CharField(blank=True, max_length=2083),
        ),
    ]
