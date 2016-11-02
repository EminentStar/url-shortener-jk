from django.shortcuts import render

from .forms import UrlForm

# Create your views here.


def main_view(request):
    form = UrlForm()
    dict_return = {}

    dict_return['form'] = form

    return render(request, 'shortener/main_view.html', dict_return)


