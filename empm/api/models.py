from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=10, unique=True)
    department = models.CharField(max_length=200)
    options = (
        ('hr','hr'),
        ('back-end developer','back-end developer'),
        ('front-end developer','front-end developer'),
        ('fullstack developer','fullstack developer')
    )
    designation = models.CharField(max_length=200,choices=options)
    phone = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    joboptions = (
        ('office','office'),
        ('wfh','wfh'),
        ('hybrid','hybrid')
    )
    jobmethod = models.CharField(max_length=200,choices=joboptions,default='office')

    def __str__(self) -> str:
        return self.name
    

class Attendance(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    date = models.DateField
    attendancestatus = models.BooleanField(default=False)
    login_time = models.TimeField()
    logout_time = models.TimeField(null=True,blank=True)
    hours = models.TimeField

    def __str__(self) -> str:
        return self.attendancestatus
    