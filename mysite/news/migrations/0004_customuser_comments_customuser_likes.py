# Generated by Django 4.0.4 on 2022-06-13 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_customuser_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='comments',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='likes',
            field=models.BigIntegerField(default=0),
        ),
    ]
