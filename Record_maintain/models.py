from django.db import models
from simple_history.models import HistoricalRecords

class employee(models.Model):
    Empid=models.IntegerField(null=True)
    Name=models.CharField(max_length=100,null=True)
    Mobile=models.BigIntegerField(null=True)
    Email=models.EmailField(max_length=50,null=True)
    Role=models.CharField(max_length=30,null=True)
    history = HistoricalRecords()

class employeefile(models.Model):
    employee = models.ForeignKey(employee, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='media/')