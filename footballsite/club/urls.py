#__author__ = 'Der Kaiser'

from django.conf.urls import  patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^simple/$', 'club.views.simple_request'),
    url(r'^template_re/$', 'club.views.template_request'),
    url(r'^temp_sim/$', 'club.views.temp_simple'),
    url(r'^all/$', 'club.views.clubs'),
    url(r'^get/(?P<club_id>\d+)/$', 'club.views.club'),
)
