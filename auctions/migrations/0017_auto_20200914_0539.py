# Generated by Django 3.0.8 on 2020-09-14 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auto_20200914_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_listings',
            name='category',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
    ]
