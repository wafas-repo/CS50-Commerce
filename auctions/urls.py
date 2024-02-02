from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("category/<str:category>/", views.category, name="category"),
     path("MyListings", views.my_listings, name="my_listings"),
    path("listings/<int:listing_id>", views.listing_page, name="listing_page"),
    path("bid/<int:listing_id>", views.bid,name="bid"),
    path("watchlist/<int:listing_id>", views.watchlist_add, name="watchlist_add"),
    path("watchlist", views.watchlist_page, name="watchlist_page"),
    path("close/<int:listing_id>", views.close, name="close"),
] 
