from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('infractions/<int:numbers>', views.infractions, name='infractions'),
    #url(r'^(?P<numbers>[\d/]+)$', views.detail)
    #path(r'<int:a>/<int:b>', views.detail, name='detail'),
    #url(r'^.*/$', views.urlke, name='urlke'),
]
