from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^logout/$',views.logout_auth,{'template_name': 'logout.html'}, name='logout'),
    url(r'^$', views.main, name='main'),
    url(r'^ajax_main/', views.ajax_main, name='ajax_main'),
    url(r'^ajax_run/', views.ajax_run, name='ajax_run'),
    url(r'about/', views.about, name='about'),
    url(r'test/', views.test, name='test'),
]

from django.conf.urls import (handler400, handler403, handler404, handler500)
handler404 = 'webapp.views.page_not_found'

# TO DO
#handler400 = 'my_app.views.bad_request'
#handler403 = 'my_app.views.permission_denied'
#handler500 = 'my_app.views.server_error'
