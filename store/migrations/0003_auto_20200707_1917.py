# Generated by Django 3.0.7 on 2020-07-07 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_store_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='store',
            name='store_img',
            field=models.CharField(default='', max_length=2000),
        ),
    ]