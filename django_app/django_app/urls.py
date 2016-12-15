from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^webapp/', include('webapp.urls')),	  # webapp as a main page, /$ nothing more than webapp/..
    url(r'^', include('personal.urls')),        # login/password -> integrate it with ldap (how?)
    #url(r'^login/', include('webapp.urls')),
]
