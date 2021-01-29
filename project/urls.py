from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('workers/', views.workers, name='workers'),
    path('', views.randomSearch, name= 'randomSearch'),
    path('result', views.result, name="result"),
    path('certification', views.certification, name="certification"),
]