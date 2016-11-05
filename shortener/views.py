from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import redis


from .forms import UrlForm
from .short_urls import create


# Create your views here.

def main_view(request):
    return HttpResponseRedirect('/create')


def create_view(request):
    form = UrlForm()
    dict_return = {}
    
    if request.method == 'POST':
        origin_url = dict(request.POST)['url'][0]
        short_url = create(origin_url)
        
        print("Original URL: %s" % (origin_url))
        print("Short URL: %s" % (short_url))

        dict_return['origin_url'] = origin_url
        dict_return['short_url'] = short_url

    dict_return['form'] = form

    return render(request, 'shortener/main_view.html', dict_return)


def shorturl_view(request, url):
    print("shorturl: %s" % (url))
    return HttpResponse(url)
    
