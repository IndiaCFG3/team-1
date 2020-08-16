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
        if(mydata['work']=='login'):
            print(users.objects.filter(username=mydata['name'],password=mydata['password']))
            course_qs = users.objects.filter(username=mydata['name'],password=mydata['password'])
            for i in course_qs:
                flag=1
        else:
            b = users(name=mydata['name'], role=mydata['role'],username=mydata['username'],email=mydata['email'],password=mydata['password'],organisation=mydata['organisation'],courseID=mydata['courseID'],courseName=mydata['courseName'])
            b.save()
            flag=1
        return Response(flag)

        
class videoList(APIView):
    def get(self,request):
        user1=video.objects.all()
        serializer=VideoSerializer(user1,many=True)
        return Response(serializer.data)

    def post(self,request):
        pass

    

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
