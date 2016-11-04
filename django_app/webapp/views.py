from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from webapp.models import DbClient, DbSystem, DbServer

import datetime
import json

#render -> we do not need to specify context_instance = RequestContext(request)
#render_to_response() -> we do 

def main(request):
    #return render(request, 'webapp/main.html')
    client_var = DbClient.objects.all()           # all() -> SELECT * FROM
    system_var = DbSystem.objects.all()
    server_var = DbServer.objects.all()
    context = {'client': client_var, 'system': system_var, 'server': server_var}  # system: aix/rhel -> not needed to display, only example
    return render(request, 'webapp/main.html', context)

def ajax_main(request):

    #server_var = DbServer.objects.values("id_client_name_id", "server_name")
    print "REQUEST--->", request.GET['key']

    server_var = DbServer.objects.filter(id_client_name_id = int(request.GET['key']))
 
    print "----------VAl--------", server_var
    # <QuerySet [<DbServer: server11>, <DbServer: server12>]>
    
    server_dic = {}
    for s in list(server_var):
        server_dic[s.id] = s.server_name
    
    return HttpResponse(json.dumps(server_dic), content_type="application/json")
    #return HttpResponse(json.dumps({"var":"ala ma kota"}), content_type="application/json")


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
