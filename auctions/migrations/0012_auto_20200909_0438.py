# Generated by Django 3.0.8 on 2020-09-09 04:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20200909_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bids',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.Auction_listings'),
        ),
        migrations.AlterField(
            model_name='bids',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
