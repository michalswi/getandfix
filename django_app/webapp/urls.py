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
