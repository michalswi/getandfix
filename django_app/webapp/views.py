from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from webapp.models import DbClient, DbSystem, DbServer, DbCommand
from ansible_django.ans_exe import get_ajax
import datetime
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.models import User
from webapp.models import DbLdap
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from . import backend
from django.views.decorators.cache import cache_control

##render -> we do not need to specify context_instance = RequestContext(request)
##render_to_response() -> we do 

USERNAME = ""

# http://stackoverflow.com/questions/35805635/after-authentication-its-not-redirecting-to-next-page-in-django
# https://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html
def login_auth(request):
  next = request.POST.get('next', request.GET.get('next', ''))
  if request.method == "POST":
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = backend.MyBackend().authenticate(username=username, password=password)
      #print "user:", user, type(user)    # USER admin <class 'django.contrib.auth.models.User'>
      if user is not None:
          # needed in main() to display logged user
          global USERNAME
          USERNAME = user
          # Redirect to a success page.  
          if user.is_active:
              login(request, user)
              if next:
                  return HttpResponseRedirect(next)
              else:
                  # after successful log in
                  return HttpResponseRedirect('/webapp')
          # Return an 'invalid login' error message.
          else:
              return HttpResponse('Inactive user')
      else:
          return HttpResponseRedirect('/')
          # by default settings.LOGIN_URL = '/accounts/login/'
          #return HttpResponseRedirect(settings.LOGIN_URL)
  return render(request, "webapp/login.html")


def logout_auth(request):
    auth.logout(request)
    # Redirect back to login page
    return HttpResponseRedirect('/')
    #return render(request, "webapp/logout.html")
"""
    print "logout / request.user.is_anonymous():", request.user.is_anonymous
    print "logout / request.user.is_authenticated():", request.user.is_authenticated
    print "logout / user:", request.user
    # required to change is_authenticated after logout from 1 to 0
    request.user.is_authenticated = False
    request.user.save()
    auth.logout(request)
    return HttpResponseRedirect('/')
"""

#login_url = '/'                -> requests are redirected for login, by default /accounts/login/
#redirect_field_name="/webapp/" -> requests are redirected after login, by default /accounts/profile
#@login_required(login_url = '/')
#cache_control, after logout user can't back to main view using "go back" button in web browser
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def main(request):

    #print "main / request.user.is_anonymous():", request.user.is_anonymous
    #print "main / request.user.is_authenticated():", request.user.is_authenticated
    #print "main / request:", request
    #print "main / user:", request.user
    #print "main / request.user.is_active:", request.user.is_active
    #print "main / request.user.id:", request.user.id

    # 'is_authenticated' is by default TRUE for real User, for Anonymous is False
    if request.user.is_authenticated:
        client_var = DbClient.objects.all()           # all() -> SELECT * FROM
        system_var = DbSystem.objects.all()
        server_var = DbServer.objects.all()
        # csrf_token related
        # main.html: to display which client was selected added: name="client_num"
        context = {'client': client_var, 'system': system_var, 'server': server_var, 'user': USERNAME}
        return render(request, 'webapp/main.html', context)
    else:
        return redirect('/', request.path)
        #return HttpResponseRedirect('/')
        #return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        #return render(request, 'myapp/login_error.html')

def ajax_main(request):
    #print "REQUEST--->", request.GET['key']
    #print 'req ->', request.GET['ajax_data_type']
    #server_var = DbServer.objects.values("id_client_name_id", "server_name")
    #server_var = DbServer.objects.filter(id_client_name_id = int(request.GET['key']))
    #print server_var
    #<QuerySet [<DbServer: server11>, <DbServer: server12>]>

    data = {}
    ## request.GET['ajax_data_type'] related to select custom in html
    if request.GET['ajax_data_type'] == 'server':
        server_var = DbServer.objects.filter(id_client_name_id = int(request.GET['key']))
        for s in list(server_var):
            data[s.id] = {'name' : s.server_name, 'ip' : s.server_ip, 'os' : s.id_os_platform_id}

    elif request.GET['ajax_data_type'] == 'command':
        command_var = DbCommand.objects.filter(id_os_platform_id = int(request.GET['key']))
        for c in list(command_var):
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
