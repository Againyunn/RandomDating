from django.urls  import path
from . import views

urlpatterns = [
        path('user/', views.user, name='user'),
        path('register/', views.register, name='register'),
        path('form/', views.form, name='form'),
        path('main/', views.main, name='main'),
        path('login/', views.login, name='login'),
]
