from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import redis


from .forms import UrlForm
from .short_urls import create
from .short_urls import shorturl


# Create your views here.

def main_view(request):
    return HttpResponseRedirect('/create')


def create_view(request):
    form = UrlForm()
    dict_return = {}

    if request.method == 'POST':
        origin_url = dict(request.POST)['url'][0]
        short_url = create(origin_url)
        host = request.META['HTTP_HOST']
        
        dict_return['origin_url'] = origin_url
        dict_return['short_url'] = host + '/' + short_url

    dict_return['form'] = form
    return render(request, 'shortener/main_view.html', dict_return)


def shorturl_view(request, url):
    print("shorturl: %s" % (url))
    origin_url = shorturl(url)

    if origin_url != "Not Found":
        if not origin_url.startswith('http'):
            origin_url = '%s%s' % ('http://', origin_url)
        return HttpResponseRedirect(origin_url)
    else:
        return HttpResponse("404 Not Found")
    
