# Generated by Django 4.0.2 on 2022-02-20 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_mymodel_caption_alter_mymodel_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='caption',
            field=models.CharField(max_length=100),
        ),
    ]
