from django.db import models

# Create your models here.
class XX(models.Model):
    title = models.CharField(verbose_name="名称", max_length=32)
    image = models.FileField(verbose_name="头像", upload_to="avatar/")

class Admin(models.Model):
    """ 管理员 """
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)

    def __str__(self):
        return self.username

class Department(models.Model):
    """ 部门表 """
    department_name = models.CharField(verbose_name="Department",max_length=100)
    
class UserInfo(models.Model):
    """ 用户表 """
    name = models.CharField(verbose_name="Name",max_length=100)
    password = models.CharField(verbose_name="Password",max_length=100)
    age = models.IntegerField(verbose_name="Age")
    account = models.DecimalField(verbose_name="Account balance", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name="Entry Time")
    
     # 无约束
    # depart_id = models.BigIntegerField(verbose_name="部门ID")
    # 1.有约束
    #   - to，与那张表关联
    #   - to_field，表中的那一列关联
    # 2.django自动
    #   - 写的depart
    #   - 生成数据列 depart_id
    # 3.部门表被删除
    # ### 3.1 级联删除
    depart = models.ForeignKey(to="Department", to_field="id", on_delete=models.CASCADE)
    # ### 3.2 置空
    # depart = models.ForeignKey(to="Department", to_field="id", null=True, blank=True, on_delete=models.SET_NULL)
    
    gender_choices = {
        (1,"male"),
        (2,"female"),
    }
    gender = models.SmallIntegerField(verbose_name = "gender",choices=gender_choices)
    
class PrettyNum(models.Model):
    """ 号表 """
    mobile = models.CharField(verbose_name="Phone number",max_length=11)
    price=models.IntegerField(verbose_name="Price",null=True,blank=True)
    
    level_choices = {
        (0,"Normal"),
        (1,"VIP1"),
        (2,"VIP2"),
        (3,"VIP3"),
    }
    
    level = models.SmallIntegerField(verbose_name="Level",choices=level_choices,default=0)
    status_choices = {
        (0,"Normal"),
        (1,"Disabled"),
    }
    status = models.SmallIntegerField(verbose_name="Status",choices=status_choices,default=0)
    
class Task(models.Model):
    """ 任务 """
    level_choices = (
        (1, "紧急"),
        (2, "重要"),
        (3, "临时"),
    )
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choices, default=1)
    title = models.CharField(verbose_name="标题", max_length=64)
    detail = models.TextField(verbose_name="详细信息")
    user = models.ForeignKey(verbose_name="负责人", to="Admin", on_delete=models.CASCADE)
    
class Order(models.Model):
    """ 订单 """
    oid = models.CharField(verbose_name="订单号", max_length=64)
    title = models.CharField(verbose_name="名称", max_length=32)
    price = models.IntegerField(verbose_name="价格")

    status_choices = (
        (1, "待支付"),
        (2, "已支付"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=1)
    # admin_id
    admin = models.ForeignKey(verbose_name="管理员", to="Admin", on_delete=models.CASCADE)


class Boss(models.Model):
    """ 老板 """
    name = models.CharField(verbose_name="姓名", max_length=32)
    age = models.IntegerField(verbose_name="年龄")
    img = models.CharField(verbose_name="头像", max_length=128)


class City(models.Model):
    """ 城市 """
    name = models.CharField(verbose_name="名称", max_length=32)
    count = models.IntegerField(verbose_name="人口")

    # 本质上数据库也是CharField，自动保存数据。
    img = models.FileField(verbose_name="Logo", max_length=128, upload_to='city/')