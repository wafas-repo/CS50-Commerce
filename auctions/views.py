from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import User, Auction_listings, Bids, Comment

from .forms import CreateListingForm, CommentForm


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Auction_listings.objects.all() # pylint: disable=maybe-no-member
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@ login_required
def create(request):
    form = CreateListingForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            print(form.errors)     
    return render(request, 'auctions/create.html', {
        "form": form
    })


def listing_page(request, listing_id):
    listing = Auction_listings.objects.get(pk=listing_id) # pylint: disable=maybe-no-member 
    comments = Comment.objects.filter(listing=listing).order_by('-id') # pylint: disable=maybe-no-member 
    added_watchlist = False

    if listing.watchlist.filter(id=request.user.id).exists():
        added_watchlist = True
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            comment = request.POST.get('comment')
            content = Comment.objects.create(listing=listing, user=request.user, comment=comment)# pylint: disable=maybe-no-member 
            content.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        comment_form = CommentForm()

    if listing.user == request.user:
        creator = True
    else:
        creator = None

    return render(request, "auctions/listing_page.html", {
        "listing": listing,
        "added_watchlist": added_watchlist,
        "creator":creator,
        "comments": comments,
        "comment_form": comment_form
    })

@ login_required(login_url='login')
def bid(request, listing_id):
    listing = Auction_listings.objects.get(pk=listing_id) # pylint: disable=maybe-no-member
    curr_bid = listing.price
    if request.method == "POST":
        if request.user.is_authenticated:
            obj = Bids()
            obj.bid = request.POST.get("bid")
            obj.listing = listing
            obj.user = request.user
            obj.save()
            bid = float(request.POST.get("bid"))
            if bid <= curr_bid:
                messages.error(request, 'Bid amount must be over the current bid amount of $' + str(curr_bid)+'0')
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
            else:
                listing = Auction_listings.objects.get(pk=listing_id)# pylint: disable=maybe-no-member
                listing.price = bid
                messages.success(request, 'You now have the current bid!')
                listing.watchlist.add(request.user)
                listing.save()
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            return HttpResponseRedirect(reverse("login"))
    return render(request, "auctions/listing_page.html", {
        "listing": listing
    })

@ login_required
def watchlist_add(request, listing_id):
    listing = Auction_listings.objects.get(pk=listing_id)# pylint: disable=maybe-no-member
    if listing.watchlist.filter(pk=request.user.id).exists():
        listing.watchlist.remove(request.user)
    else:
        listing.watchlist.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@ login_required
def watchlist_page(request):
    user = request.user
    listings = user.watchlist.all()
    context = {
        'listings':listings
    }
    return render(request, "auctions/watchlist.html", context)

@ login_required
def close(request, listing_id):
    listing = Auction_listings.objects.get(pk=listing_id)# pylint: disable=maybe-no-member
    if request.method == "POST":
        if listing.user == request.user:
            listing.active = False
            listing.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def category(request,category):
    category_listings = Auction_listings.objects.filter(category=category, active=True) # pylint: disable=maybe-no-member
    return render(request,"auctions/category.html",{
        "category_listings":category_listings,
        "cat":category,
    })

def my_listings(request):
    my_list = Auction_listings.objects.filter(user=request.user)# pylint: disable=maybe-no-member
    print(my_list)
    return render(request, "auctions/my_listings.html",{
        "my_list": my_list
    })

