# Generated by Django 4.0.2 on 2022-02-22 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_mymodel_caption'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mymodel',
            options={'ordering': ['id'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='caption',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Обновленно'),
        ),
    ]