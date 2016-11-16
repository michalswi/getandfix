from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext, loader

from webapp.models import DbClient, DbSystem, DbServer

import datetime
import json

##render -> we do not need to specify context_instance = RequestContext(request)
##render_to_response() -> we do 

def main(request):
    #return render(request, 'webapp/main.html')
    client_var = DbClient.objects.all()           # all() -> SELECT * FROM
    system_var = DbSystem.objects.all()
    server_var = DbServer.objects.all()

    #print client_var, type(client_var)
    context = {'client': client_var, 'system': system_var, 'server': server_var}  # system: aix/rhel -> not needed to display, only example
    return render(request, 'webapp/main.html', context)

def ajax_main(request):

    print "REQUEST--->", request.GET['key']
    print 'req ->', request.GET['ajax_data_type']

    #server_var = DbServer.objects.values("id_client_name_id", "server_name")

    #server_var = DbServer.objects.filter(id_client_name_id = int(request.GET['key']))
    #print server_var
    #<QuerySet [<DbServer: server11>, <DbServer: server12>]>

    """
    server_dic = {}
    for s in list(server_var):
        server_dic[s.id] = s.server_name
    #data = json.dumps(server_dic)
    print "data----->", data
    """
    server_dic = {}
    ## request.GET['ajax_data_type'] related to select custom in html
    if request.GET['ajax_data_type'] == 'server':
        server_var = DbServer.objects.filter(id_client_name_id = int(request.GET['key']))
        for s in list(server_var):
            server_dic[s.id] = {'name' : s.server_name, 'ip' : s.server_ip, 'os' : s.id_os_platform_id}
    else:       # request.GET['ajax_data_type'] == 'command'
        pass

    print server_dic
    ## JsonResponse takes dict not json
    return JsonResponse(server_dic, content_type="application/json")
    #return JsonResponse({1:{"var":"ala ma kota"}}, content_type="application/json")
    #return HttpResponse(data, content_type="application/json")
    #return HttpResponse(json.dumps('{"var":"ala ma kota"}'), content_type="application/json")

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
