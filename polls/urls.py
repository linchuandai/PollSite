from django.conf.urls import url

#import views from current directory
from . import view

urlpatterns = [
    url(r'^$', view.index, name='index'),

]
