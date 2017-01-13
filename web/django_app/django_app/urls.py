from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
import webapp.views

urlpatterns = [
    url(r'^$', webapp.views.login_auth),          # it's referring to webapp.views.login_auth
    url(r'^logout/$', webapp.views.logout_auth),
    #url(r'^logout/$',auth_views.logout),         # built-in method
    url(r'^webapp/', include('webapp.urls')),     # webapp as a main page, /$ nothing more than webapp/..
    url(r'^admin/', admin.site.urls),
]
