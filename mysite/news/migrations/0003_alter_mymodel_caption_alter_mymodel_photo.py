# Generated by Django 4.0.2 on 2022-02-15 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_mymodel_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='caption',
            field=models.CharField(max_length=22),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='photo',
            field=models.ImageField(height_field=500, upload_to='media/', width_field=500),
        ),
    ]
