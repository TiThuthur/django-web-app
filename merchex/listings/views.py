from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.mail import send_mail

from listings.models import (Band, Listing)
from listings.forms import ContactUsForm, BandForm


# Create your views here.


def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band.html",
                  {"bands": bands})


def band_detail(request, band_id):
    band = get_object_or_404(Band, pk=band_id)
    return render(request,
                  "listings/band_detail.html",
                  {"band": band})


def about(request):
    return render(request, "listings/about-us.html",
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
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(subject=f"""Message from {form.cleaned_data['name'] or "anonyme"} via MerchEx ContactUs form""",
                      message=form.cleaned_data['message'],
                      from_email=form.cleaned_data["email"],
                      recipient_list=["admin@merchex.xyz"], )
        return redirect("email_sent")
    else:
        #si ce n'est pas une request POST alors c'est une request GET
        form = ContactUsForm()

    return render(request, "listings/contact.html",
                  {"form": form})


def page_not_found(request, exception):
    return render(request, "listings/404.html", {"exception": exception}, status=404)


def email_sent(request):
    return render(request, "listings/email-sent.html", {"message": "votre message a bien été envoyé."})


def band_create(request):
    if request.method == "POST":
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect("band_detail", band.id)
    else:
        form = BandForm()
    return render(request, "listings/band_create.html", {"form": form})
