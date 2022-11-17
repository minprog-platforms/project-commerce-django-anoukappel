from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Bids, Comments


def index(request):
    return render(request, "auctions/index.html", {
        "auctions" : Listing.objects.all()
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

def create_listing(request):
    if request.method == "GET":
        return render(request, "auctions/new_listing.html")
    else:
        # Save new listing in database
        title = request.POST["title"]
        description = request.POST["description"]
        price = request.POST["price"]
        image = request.POST["image"]

        new_list = Listing(title=title, description=description, price=price, image=image)
        new_list.save()

        return render(request, "auctions/new_listing.html")


def auction(request, title):
    auction = Listing.objects.get(title=title)
    if request.method == "GET":
        return render(request, "auctions/display_auction.html", {
            "title": auction.title,
            "description": auction.description,
            "price": auction.price,
            "image": auction.image,
            "biedingen" : Bids.objects.all(),
            "comment": Comments.objects.all()
        })
    else:
        # save het nieuwe bod
        new_bod = request.POST["new_bod"]
        bod = Bids(listing = auction, new_bid = new_bod)
        bod.save()
        # save de nieuwe comment
        new_comment =  request.POST["comment"]
        comment = Comments(listing = auction, new_comment=new_comment)
        comment.save()
        return render(request, "auctions/index.html", {
            "auctions" : Listing.objects.all()
        })
