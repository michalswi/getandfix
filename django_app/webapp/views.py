from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from webapp.models import DbClient, DbSystem, DbServer, DbCommand

from ansible_django.ans_exe import get_ajax
from ldap_stuff.use_ldap import run_main

import datetime
import json


# http://stackoverflow.com/questions/35805635/after-authentication-its-not-redirecting-to-next-page-in-django
# https://codedump.io/share/WsUv4qLpNA2w/1/django---login-and-redirect-to-user-profile-page
# https://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html

# AUTH
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication

# KEEP SESSION
# https://docs.djangoproject.com/en/1.10/topics/http/sessions/
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Sessions


from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.models import User

from webapp.models import DbLdap

from django.views.decorators.cache import cache_control

from django.contrib.auth.decorators import login_required

##render -> we do not need to specify context_instance = RequestContext(request)
##render_to_response() -> we do 

USERNAME = ""

def f(u, p):
  print u, p
  return True
 
# auth.authenticate(username=username, password=password)
# https://docs.djangoproject.com/en/1.10/topics/auth/customizing/
class MyBackend(object):
  def authenticate(self, username=None, password=None):
    #if f(username, password):
    if run_main(username, password):
        # run_main checks first in DbLdap if user is there (based on email) if not will add
        user = DbLdap.objects.get(user_email=username)
        return user
    return None

def login_auth(request):
  print "#login_auth"
  next = request.POST.get('next', request.GET.get('next', ''))
  if request.method == "POST":
      username = request.POST.get('username')
      password = request.POST.get('password')
      #user = auth.authenticate(username=username, password=password)
      user = MyBackend().authenticate(username=username, password=password)
      print "USER", user, type(user)    # USER admin <class 'django.contrib.auth.models.User'>
      if user != None:

          # needed in main() to display logged user
          global USERNAME
          USERNAME = user

          if user.is_active:
              login(request, user)
              if next:
                  return HttpResponseRedirect(next)
              return HttpResponseRedirect('/webapp')
          else:
              return HttpResponse('Inactive user')
      else:
          return HttpResponseRedirect('/')       
          #return HttpResponseRedirect(settings.LOGIN_URL)      # by default settings.LOGIN_URL = '/accounts/login/'
  return render(request, "webapp/login.html")

def logout_auth(request):
    auth.logout(request)
    # Redirect back to login page
    #return HttpResponseRedirect('/')
    return render(request, "webapp/logout.html")

@login_required
def main(request):
    print "#main"
    print "request:", request
    print request.user.is_authenticated
    #user.is_authenticated is by default TRUE
    if not request.user.is_authenticated:
        print "else main"
        client_var = DbClient.objects.all()           # all() -> SELECT * FROM
        system_var = DbSystem.objects.all()
        server_var = DbServer.objects.all()

        # csrf_token related
        # main.html: to display which client was selected added: name="client_num"

        #print client_var, type(client_var)
        context = {'client': client_var, 'system': system_var, 'server': server_var, 'user': USERNAME}
        return render(request, 'webapp/main.html', context)

    else:
        print "if main"
        return redirect('/', request.path)
        #return HttpResponseRedirect('/')
        #return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        #return render(request, 'myapp/login_error.html')

def ajax_main(request):

    print "REQUEST--->", request.GET['key']
    print 'req ->', request.GET['ajax_data_type']

    #server_var = DbServer.objects.values("id_client_name_id", "server_name")

    #server_var = DbServer.objects.filter(id_client_name_id = int(request.GET['key']))
    #print server_var
    #<QuerySet [<DbServer: server11>, <DbServer: server12>]>

    #server_dic = {}
    #command_dic = {}
    data = {}
    ## request.GET['ajax_data_type'] related to select custom in html
    if request.GET['ajax_data_type'] == 'server':
        server_var = DbServer.objects.filter(id_client_name_id = int(request.GET['key']))
        for s in list(server_var):
            #server_dic[s.id] = {'name' : s.server_name, 'ip' : s.server_ip, 'os' : s.id_os_platform_id}
            data[s.id] = {'name' : s.server_name, 'ip' : s.server_ip, 'os' : s.id_os_platform_id}

    elif request.GET['ajax_data_type'] == 'command':
        command_var = DbCommand.objects.filter(id_os_platform_id = int(request.GET['key']))
        for c in list(command_var):
            #command_dic[c.id] = c.cmd
            data[c.id] = c.cmd
    print data
    ## JsonResponse takes dict not json
    return JsonResponse(data, content_type="application/json")

def ajax_run(request):
    #print 'ajax_run:', request.GET.items()
    #ajax_run: [(u'command_val', u'4'), (u'server_val', u'1'), (u'client_val', u'1')]
    data = get_ajax(request.GET.items())
    return HttpResponse(data, content_type='text/plain')

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
