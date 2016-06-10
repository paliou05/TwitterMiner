from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'home', views.home, name='home'),
    url(r'stream', views.stream, name= 'stream'),
    url(r'index', views.index, name='index'),
    url(r'get_top_users',views.get_top_users, name='get_top_users')
    #url(r'submit', views.submit, name='submit'),
    #url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    #url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
]