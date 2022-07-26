from django.shortcuts import render
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