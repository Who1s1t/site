# Generated by Django 4.0.2 on 2022-02-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(default=None, max_length=22)),
                ('text', models.TextField(default=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(default='/media/img.png', height_field=500, upload_to='media/', width_field=500)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
