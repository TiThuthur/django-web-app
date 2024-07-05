from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from listings.models import (Band, Listing)
from listings.forms import ContactUsForm


# Create your views here.


def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band.html",
                  {"bands": bands})


def band_details(request, band_id):
    band = get_object_or_404(Band, pk=band_id)
    return render(request,
                  "listings/band_detail.html",
                  {"band": band})


def about(request):
    return render(request, "listings/about.html",
                  {
                      "H1": "A propos",
                      "message": "Nous adorons merch !"
                  })


def listing(request):
    listings = Listing.objects.all()
    return render(request, "listings/listings.html",
                  {"listings": listings})


def listing_details(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    return render(request,
                  "listings/listings_details.html",
                  {"listing": listing})


def contact(request):
    print("La méthode de requête est : ", request.method)
    print("Les données POST sont : ", request.POST)
    form = ContactUsForm()
    return render(request, "listings/contact.html",
                  {"form": form})


def page_not_found(request, exception):
    return render(request, "listings/404.html", {"exception": exception}, status=404)
