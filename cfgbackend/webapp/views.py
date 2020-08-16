from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import users,Course
from . serializers import UserSerializer
from datetime import date

class userList(APIView):
    def get(self,request):
        user1=users.objects.all()
        serializer=UserSerializer(user1,many=True)
        return Response(serializer.data)

    def post(self):
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
