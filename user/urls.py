from django.urls  import path
from . import views

urlpatterns = [
        path('user', views.user, name='user'),
        path('form/', views.form, name='form'),
]
