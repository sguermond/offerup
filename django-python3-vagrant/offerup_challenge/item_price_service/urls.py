from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_item),
    #Question to ask Dustin: do I actually need a form page at the index for searches,
    #or are all searches done through the URL?
    #url(r'^$', views.index, name='index'),
]
