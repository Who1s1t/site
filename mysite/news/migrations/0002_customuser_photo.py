# Generated by Django 4.0.4 on 2022-05-31 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(blank=True, upload_to='news/user/%Y/%m/%d'),
        ),
    ]
