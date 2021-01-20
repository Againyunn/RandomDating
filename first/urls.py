from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
urlpatterns = [
        path('index' ,views.index, name='index'),
        path('worksheet' ,views.worksheet, name='worksheet'),
        path('test' ,views.test, name='test'),
        path('gugu', views.gugu, name='gugu'),
]
