# Generated by Django 3.0.7 on 2020-07-02 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20200702_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeorder',
            name='status',
            field=models.IntegerField(choices=[(0, 'Processing'), (1, 'Completed')], default=0),
        ),
    ]
