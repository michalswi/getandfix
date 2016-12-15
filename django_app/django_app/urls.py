from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'webapp/login.html'}, name='login'),
    url(r'^logout/$', auth_views.login, name='logout'),
    url(r'^admin/', admin.site.urls),
    #url(r'^webapp/', include('webapp.urls')),	  # webapp as a main page, /$ nothing more than webapp/..
    #url(r'^', include('personal.urls')),        # login/password -> integrate it with ldap (how?)
]
