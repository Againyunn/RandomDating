from django.db import models

# Create your models here.
class Members(models.Model):
    username = models.CharField(max_length=64, verbose_name="사용자")
    useremail = models.EmailField(max_length=128, verbose_name="이메일")
    
    class Meta:
        db_table = "jaeyun_users"



