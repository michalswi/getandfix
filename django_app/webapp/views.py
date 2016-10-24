from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from webapp.models import DbClient
import datetime

def index(request):
    #return render(request, 'webapp/main.html')
    test_var = DbClient.objects.get().client_name
    context = {'client': test_var}
    return render(request, 'webapp/main.html', context)

#def test(request):
#    return render(request, 'webapp/test.html')

def test(request):
    #now = datetime.datetime.now()
    #context = {'current_date': now}
    #return render(request, 'webapp/test.html', context)        
    test_var = DbClient.objects.get().client_name
    context = {'client': test_var}
    return render(request, 'webapp/test.html', context)

def about(request):
    t = loader.get_template('webapp/about.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))
