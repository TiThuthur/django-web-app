from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from listings.models import (Band, Listing)


# Create your views here.


def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band.html",
                  {"bands": bands})


def band_details(request, band_id):
    band = get_object_or_404(Band, pk=band_id)
    #band = Band.objects.get(id=band_id)
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


def contactus(request):
    return render(request, "listings/contact.html",
                  {
                      "H1": "contactez-nous !",
                  })


def page_not_found(request, exception):
    return render(request, "listings/404.html", {"exception": exception}, status=404)
