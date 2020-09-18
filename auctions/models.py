from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Max


class User(AbstractUser):
    pass

class Auction_listings(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    price = models.FloatField()
    image = models.CharField(null=True, blank=True, max_length=165)
    time_posted = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category = models.CharField(max_length=64, default=None, blank=True, null=True)
    watchlist = models.ManyToManyField(User, related_name='watchlist', blank=True)
    active = models.BooleanField(default=True)

    def winning_bid(self):
        return max([bid.bid for bid in self.bids.all()]+[self.price])# pylint: disable=maybe-no-member

    def winner(self):
        return self.bids.get(bid=self.winning_bid()).user if len(self.bids.all()) > 0 else None# pylint: disable=maybe-no-member

    def __str__(self):
        return self.title 
    

class Bids(models.Model):
    bid = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    listing = models.ForeignKey(Auction_listings, on_delete=models.CASCADE, related_name="bids")

    def __str__(self):
        return '$ %s bid on listing %s by %s' % (self.bid, self.listing, self.user)

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    listing = models.ForeignKey(Auction_listings, on_delete=models.CASCADE, related_name="comments")
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.listing.title, self.user)# pylint: disable=maybe-no-member

class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    

