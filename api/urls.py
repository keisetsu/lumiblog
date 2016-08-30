from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^entry/$', views.EntryList.as_view()),
    url(r'^entry/(?P<pk>[0-9]+)/$', views.EntryDetail.as_view()),
]
