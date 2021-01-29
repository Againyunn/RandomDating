from django.db import models

# Create your models here.
class Project(models.Model):
    userid = models.CharField(max_length=64, verbose_name='아이디')
    username = models.CharField(max_length=64, verbose_name='사용자명')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    GENDERS = (('M','남성(Man)'),('W','여성(Woman)'))
    gender = models.CharField(max_length=1, verbose_name='성별', choices=GENDERS)
    registered = models.DateTimeField(auto_now_add=True, verbose_name='등록')

#class Account(models.Model):