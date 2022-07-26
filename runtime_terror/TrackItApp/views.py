from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
# from pymysql import *
# from pymysql import cursors

# Create your views here.
def show(request):
    cursor=connection.cursor()
    cursor.execute('select * from student where softdelete=0')
    columns=[col[0] for col in cursor.description]
    info=[
        dict(zip(row,columns))
        for row in cursor.fetchall()
    ]
    print(info)
    context={
        'keyinfo':info
    }
    # return HttpResponse('hello world')
    return render(request,'TrackItApp/login.html',context)

# def second(request):
#     return render(request,'TrackItApp/second.html')
def fetch(request):
    username=request.POST['username']
    password=request.POST['password']
    print(username,password)
    cursor=connection.cursor()
    cursor.execute('select * from faculty where fname=%s and f_pwd=%s',(username,password))
    result=cursor.fetchone()
    print(result)
    if result is None:
        return HttpResponse('invalid user')
    else:
        return render(request,'TrackItApp/second.html')

def back(request):
    # return redirect('report')
    return render(request,'TrackItApp/login.html')
    # return HttpResponse('hellooooooo')

def keep(request):
    grade=request.POST.get('standard')
    sname=request.POST.get('sname')
    roll_no=request.POST.get('roll_no')
    print(grade,sname,roll_no)
    cursor=connection.cursor()
    # cursor.execute('select * from student where grade=%s and roll_no=%d',(grade,roll_no))
    cursor.execute('select * from student where grade=%s and roll_no=%s',(grade,roll_no))
    result=cursor.fetchone()
    print(result)
    return HttpResponse('hello world')
