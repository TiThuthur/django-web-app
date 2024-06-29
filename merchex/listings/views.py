from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Article

# Create your views here.


def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django!</h1>
        <p>Mes groupes du moments:</p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
        """)


def about(request):
    return HttpResponse("<h1>A propos</h1> <p>Nous adorons merch !</p>")


def listings(request):
    article = Article.objects.all()
    return HttpResponse(f"""<h1> liste d'articles</h1>
                        <p>{article[0].title}</p>
                        <p>{article[1].title}</p>
                        <p>{article[2].title}</p>
                        """)


def contactus(request):
    return HttpResponse("<h1>contactez-nous !</h1>")