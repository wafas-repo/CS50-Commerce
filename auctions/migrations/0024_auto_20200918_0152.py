# Generated by Django 3.0.8 on 2020-09-18 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_auto_20200917_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_listings',
            name='image',
            field=models.CharField(blank=True, max_length=165, null=True),
        ),
    ]
