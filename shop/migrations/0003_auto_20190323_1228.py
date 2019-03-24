# Generated by Django 2.0.7 on 2019-03-23 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_offers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Offers',
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(),
        ),
    ]