from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from webapp.models import DbClient, DbSystem
import datetime

#render -> we do not need to specify context_instance = RequestContext(request)
#render_to_response() -> we do 

def index(request):
    #return render(request, 'webapp/main.html')
    client_var = DbClient.objects.all()           # all() -> SELECT * FROM
    system_var = DbSystem.objects.all()
    context = {'client': client_var, 'system': system_var}
    return render(request, 'webapp/main.html', context)


def test(request):
    #return render(request, 'webapp/test.html')

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

# In progress
# https://www.safaribooksonline.com/library/view/django-web-development/9781787121386/ch06s02.html
