from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #url(r'^(?P<numbers>[\d/]+)$', views.detail)
    #path(r'<int:a>/<int:b>', views.detail, name='detail'),
    #url(r'^.*/$', views.urlke, name='urlke'),
]
