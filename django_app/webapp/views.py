from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
    return render(request, 'webapp/main.html')

def test(request):
    return render(request, 'webapp/test.html')

def about(request):
    t = loader.get_template('webapp/about.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))
