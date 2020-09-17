from django.contrib import admin

from .models import Auction_listings, Bids, Comment, Category, User

# Register your models here.
admin.site.register(Auction_listings)
admin.site.register(Bids)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(User)