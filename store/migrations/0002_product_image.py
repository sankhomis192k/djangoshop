# Generated by Django 2.0 on 2020-05-05 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
