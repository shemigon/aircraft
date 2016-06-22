from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.AircraftListView.as_view()),
    url(r'^(?P<pk>\d+)/$', views.AircraftDetailView.as_view()),
]
