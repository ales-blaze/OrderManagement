# Generated by Django 2.0.7 on 2019-03-23 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20190323_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.URLField(max_length=255),
        ),
    ]
