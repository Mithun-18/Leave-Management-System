from django.db import models
# Create your models here.
class User(models.Model):
    user_id =models.CharField(max_length=10)
    name =models.CharField(max_length=24)
    password =models.TextField(max_length=128)
    
    def __str__(self) -> str:
        return self.name
        
class Students(models.Model):
    user_id =models.CharField(max_length=10)
    date_from=models.DateField()
    date_to=models.DateField()
    leave_type=models.CharField(max_length=8)
    reason=models.TextField(max_length=200)
    total_days=models.IntegerField()
    status=models.CharField(max_length=12,default='Pending')
    
    def __str__(self) -> str:
        return self.user_id