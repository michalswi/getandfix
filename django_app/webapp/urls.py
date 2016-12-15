from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^login/$', views.index, name='index'),
    #url(r'^login/$', auth_views.login, {'template_name': 'webapp/login.html'}, name='login'),
    url(r'^login/$', auth_views.login, name='login'),
    #url(r'^$', views.main, name='main'),
    url(r'^webapp/$', views.main, name='main'),
    url(r'^ajax_main/$', views.ajax_main, name='ajax_main'),
    url(r'^ajax_run/$', views.ajax_run, name='ajax_run'),
    url(r'about/$', views.about, name='about'),
    url(r'test/$', views.test, name='test'),
]
