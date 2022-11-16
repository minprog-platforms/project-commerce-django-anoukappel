# Application Name

Design an eBay-like e-commerce auction site that will allow users to post auction listings, place bids on listings, comment on those listings, and add listings to a “watchlist.”


## Getting Started
CREATE LISTING PAGE: \
Users should be able to visit a page to  create a new listing,
where they can specify title, text-based description, starting bid.
Optional: provide image of listing and / or catergory.
![This is an image](/afbeeldingen/create_listing.jpg)

ACTIVE LISTING PAGE: \
default route of web application. \
Should let users view all the currently active listings. \
For each listing, this page should display title, description, current price, and photo ( if available)
![This is an image](/afbeeldingen/active_listing.jpg)

LISTING PAGE:
page specific for that listing: \
View alle details of listing including current price.
If logged in:
1. user is able to add to watch list
2. bid on the item
3. is user created the listing he should be able to close the listing
4. if user logged in on closed listing page and user has won auction the page should say so.
5. users should be able to add comment.
![This is an image](/afbeeldingen/listing_page_ingelogd.jpg)

![This is an image](/afbeeldingen/listing_page_niet_ingelogd.jpg)

### models
1. User model .
2. Auction listing.
3. bids.
4. comments made on auction listing.
