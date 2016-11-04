from django.shortcuts import render

from .forms import UrlForm

# Create your views here.


def main_view(request):
    form = UrlForm()
    dict_return = {}
    
    if request.method == 'POST':
        origin_url = dict(request.POST)['url'][0]
        print("Original URL: %s" % (origin_url))
        dict_return['origin_url'] = origin_url

    dict_return['form'] = form

    return render(request, 'shortener/main_view.html', dict_return)


