# Generated by Django 3.1.2 on 2020-11-08 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_category_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.FileField(blank=True, null=True, upload_to='blog/post/thumbnail'),
        ),
    ]