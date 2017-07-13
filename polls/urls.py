from django.conf.urls import url

#import views from current directory
from . import view

app_name = 'polls'

urlpatterns = [
    url(r'^$', view.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', view.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', view.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', view.vote, name='vote'),

]
