# Generated by Django 3.0.8 on 2020-09-08 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auction_listings_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_listings',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
