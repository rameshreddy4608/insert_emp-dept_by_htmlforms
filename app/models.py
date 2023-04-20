from django.db import models

# Create your models here.
class DEPARTMENT(models.Model):
   deptno=models.IntegerField(primary_key=True)
   dname=models.CharField(max_length=100,unique=True)
   loc=models.CharField(max_length=100)
   
   def __str__(self):
    return str(self.deptno)


class EMPLOYEE(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    mgr=models.IntegerField(default=0)
    hiredate=models.DateField()
    sal=models.IntegerField()
    comm=models.IntegerField()
    deptno=models.ForeignKey(DEPARTMENT,on_delete=models.CASCADE,default=True)

    def __str__(self):
        return self.ename