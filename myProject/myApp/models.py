from django.db import models

# Create your models here.
class Employee(models.Model):
 empName = models.CharField('Name ',max_length=50)
 empAge = models.IntegerField('Age ')
 empAddress = models.TextField('Address ')
 empJoinDate = models.DateTimeField("Join Date")
 empJoinDate = models.DateTimeField("Join Date")

 def __str__(self):
  return self.empName

class Client(models.Model):
 clientName = models.CharField('Name', max_length=50)
 clientAge = models.IntegerField('Age')
 clientWeight = models.DecimalField('Weight (kg)',decimal_places=2,max_digits=5)
 clientHeight = models.DecimalField('Height (cm)',max_digits=5,decimal_places=2)
 clientAddress = models.TextField('Address')
 clientJoinDate = models.DateField('Join Date')
 clientPlan = models.CharField('Plan', max_length=50)

 def __str__(self):
  return self.clientName

  

