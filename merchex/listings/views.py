from django.shortcuts import render
from django.http import HttpResponse

from listings.models import (Band, Listing)


# Create your views here.


def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/hello.html",
                  {"bands": bands})


def about(request):
    return render(request, "listings/about.html",
                  {
                      "H1":"A propos",
                      "message": "Nous adorons merch !"
                      })


def listing(request):
    listings = Listing.objects.all()
    return render(request,"listings/listings.html",
                  {"listings":listings})


def contactus(request):
    return render(request, "listings/contact.html",
                  {
                      "H1": "contactez-nous !",
                  })
