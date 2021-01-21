from django.urls  import path
from . import views

urlpatterns = [
        path('user/', views.user, name='user'),
        path('register/', views.register, name='register'),
        path('form/', views.form, name='form'),
        path('main/', views.main, name='main'),
        path('login/', views.login, name='login'),
        path('calender/', views.calender, name='calender'),
        path('<int:question_id>/' , views.detail, name="detail"), #숫자 형태로 입력받는 경우 모두 veiws.detail을 실행
]
