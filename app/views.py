from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from app.models import *

def Insert_DEPARTMENT(request):
    if request.method=='POST':
        deptno=request.POST['deptno']
        dname=request.POST['dname']
        loc=request.POST['loc']
        DNO=DEPARTMENT.objects.get_or_create(deptno=deptno,dname=dname,loc=loc)[0]
        DNO.save()
        return HttpResponse('Inserted DEPARTMENT sucessfully')
    return render(request,'Insert_DEPARTMENT.html')



def Insert_EMPLOYEE(request):
    ITO=DEPARTMENT.objects.all()
    d={'topic':ITO}
    if request.method=='POST':
        empno=request.POST['empno']
        ename=request.POST['ename']
        job=request.POST['job']
        mgr=request.POST['mgr']
        hiredate=request.POST['hiredate']
        sal=request.POST['sal']
        comm=request.POST['comm']
        deptno=request.POST['deptno']
        # dname=request.POST['dname']
        # loc=request.POST['loc']

        DNO=DEPARTMENT.objects.get_or_create(deptno=deptno)[0]
        DNO.save()
        ENO=EMPLOYEE.objects.get_or_create(deptno=DNO,empno=empno,ename=ename,job=job,mgr=mgr,hiredate=hiredate,sal=sal,comm=comm)[0]
        ENO.save()
        return HttpResponse('Inserted Employee data sucessfully')
    return render(request,'Insert_EMPLOYEE.html',d)

