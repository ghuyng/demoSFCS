# Generated by Django 3.0.7 on 2020-07-04 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_auto_20200705_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeorder',
            name='status',
            field=models.CharField(choices=[('P', 'Processing'), ('C', 'Completed')], default='P', max_length=2),
        ),
    ]
