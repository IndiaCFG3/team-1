from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import UserSerializer,VideoSerializer
import ast
from django.shortcuts import render,redirect
from . models import users,Course,video
from datetime import date


class userList(APIView):
    def get(self,request):
        user1=users.objects.all()
        serializer=UserSerializer(user1,many=True)
        return Response(serializer.data)

    def post(self,request):
    
        dict_str = request.body.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        flag=0
        print(mydata)
        if(mydata['work']=='login'):
            print(mydata)
            print(users.objects.filter(username=mydata['name'],password=mydata['password']))
            course_qs = users.objects.filter(username=mydata['name'],password=mydata['password'])
            for i in course_qs:
                flag=1
            
        else:
            b = users(name=mydata['name'], role=mydata['role'],username=mydata['username'],email=mydata['email'],password=mydata['password'],organisation=mydata['organisation'],courseID=mydata['courseID'],courseName=mydata['courseName'])
            b.save()
            print(mydata)
            flag=1
        return Response(flag)
    
    
    
 

        
class videoList(APIView):
    def get(self,request):
        user1=video.objects.all()
        serializer=VideoSerializer(user1,many=True)
        return Response(serializer.data)

    def post(self,request):
        if(request.method=="POST"):
            dict_str = request.body.decode("UTF-8")
            mydata = ast.literal_eval(dict_str)
            print(mydata['url'])
            video.objects.create(url=mydata['url'],courseName="App Development",courseID="Afwjb1k23",moduleName="Getting Started")
            return Response('Saved')
       

    

def createCourse(request):
    if(request.method=="POST"):
        cname=request.POST.get('cname')
        des=request.POST.get('desc')
        C_date=date.today()
        validity=request.POST.get('val')
        user=request.user
        Course.objects.create(name=cname,description=des,no_of_students=0,Course_creation=C_date,Validity=validity,user=user)
        return(HttpResponse('Saved'))
    else:
        return(HttpResponse('Saved not'))


def Dashboard(request):
    return(HttpResponse("DashBoard"))


def index(request):
    return(render(request,'index.html'))


def uploadVideo(request):
    if(request.method=="POST"):

        QT1=request.POST.get('q1')
        QT1A=request.POST.get('q1-A')
        QT1B = request.POST.get('q1-B')
        QT1C= request.POST.get('q1-C')
        QT1D = request.POST.get('q1-D')
        QT1CA= request.POST.get('q1-ans')
        Q1=Question.objects.create(question_text=QT1,opt_1=QT1A,opt_2=QT1B,opt_3=QT1C,opt_4=QT1D,video_id=Vid,correct_answer=QT1CA)

        QT2 = request.POST.get('q2')
        QT2A = request.POST.get('q2-A')
        QT2B = request.POST.get('q2-B')
        QT2C = request.POST.get('q2-C')
        QT2D = request.POST.get('q2-D')
        QT2CA= request.POST.get('q2-ans')
        Q2=Question.objects.create(question_text=QT2,opt_1=QT2A,opt_2=QT2B,opt_3=QT2C,opt_4=QT2D,video_id=Vid,correct_answer=QT2CA)

        QT3 = request.POST.get('q3')
        QT3A = request.POST.get('q3-A')
        QT3B = request.POST.get('q3-B')
        QT3C = request.POST.get('q3-C')
        QT3D = request.POST.get('q3-D')
        QT3CA= request.POST.get('q3-ans')
        Q3=Question.objects.create(question_text=QT3,opt_1=QT3A,opt_2=QT3B,opt_3=QT3C,opt_4=QT3D,video_id=Vid,correct_answer=QT3CA)

        return (HttpResponse('Saved'))
    else:
        return (HttpResponse('Saved not'))

def uploadVideoBE(request):
    if(request.method=="POST"):

        QT1=request.POST.get('q1')
        QT1A=request.POST.get('q1-A')
        QT1B = request.POST.get('q1-B')
        QT1C= request.POST.get('q1-C')
        QT1D = request.POST.get('q1-D')
        QT1CA= request.POST.get('q1-ans')
        Q1=Question.objects.create(question_text=QT1,opt_1=QT1A,opt_2=QT1B,opt_3=QT1C,opt_4=QT1D,video_id=Vid,correct_answer=QT1CA)

        QT2 = request.POST.get('q2')
        QT2A = request.POST.get('q2-A')
        QT2B = request.POST.get('q2-B')
        QT2C = request.POST.get('q2-C')
        QT2D = request.POST.get('q2-D')
        QT2CA= request.POST.get('q2-ans')
        Q2=Question.objects.create(question_text=QT2,opt_1=QT2A,opt_2=QT2B,opt_3=QT2C,opt_4=QT2D,video_id=Vid,correct_answer=QT2CA)

        QT3 = request.POST.get('q3')
        QT3A = request.POST.get('q3-A')
        QT3B = request.POST.get('q3-B')
        QT3C = request.POST.get('q3-C')
        QT3D = request.POST.get('q3-D')
        QT3CA= request.POST.get('q3-ans')
        Q3=Question.objects.create(question_text=QT3,opt_1=QT3A,opt_2=QT3B,opt_3=QT3C,opt_4=QT3D,video_id=Vid,correct_answer=QT3CA)

        return (HttpResponse('Saved'))
    else:
        return (HttpResponse('Saved not'))


