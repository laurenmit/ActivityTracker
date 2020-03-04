from django.urls import path

from . import views
from django.urls import include, path


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('results', views.ResultsView.as_view(), name='results'),


]
