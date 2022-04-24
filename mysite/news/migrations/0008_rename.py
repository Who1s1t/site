from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_mymodel_category'),
    ]

    operations = [
        migrations.RenameModel('MyModel', 'News')
    ]