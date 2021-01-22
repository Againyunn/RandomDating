from django.urls  import path
from . import views

urlpatterns = [
        path('<str:charactor1>/<str:charactor2>/' , views.detail, name="detail"), 
        path('', views.error , name='error'),
]
