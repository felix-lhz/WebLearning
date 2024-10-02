from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(null = True , blank=True) #null=True表示数据库中可以为空，blank=True表示表单中可以为空 
    email = models.CharField(max_length=32)
    user_type_choices = (
        (1, "普通用户"),
        (2, "VIP"),
        (3, "SVIP"),
    )
    user_type = models.IntegerField(choices=user_type_choices)
    