from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows/new$', views.AddShowView),
    url(r'^shows$', views.AllShows),
    url(r'^shows/(?P<id>\d+)/edit$', views.EditShowView),
    url(r'^shows/(?P<id>\d+)$', views.ShowView),
    url(r'^add_show', views.AddShow),
    url(r'^edit_show/(?P<id>\d+)$', views.EditShow),
    url(r'^delete_show/(?P<id>\d+)$', views.DeleteShow)


]