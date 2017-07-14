from django.conf.urls import url

#import views from current directory
from . import view

app_name = 'polls'

#pk = Primary Key

urlpatterns = [
    url(r'^$', view.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', view.DetailView.as_view, name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', view.DetailView.as_view, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', view.vote, name='vote'),

]
