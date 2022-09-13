# from http.client import HTTPResponse
from re import A
from django.shortcuts import render,redirect
from myApp.models import Employee
from myApp.models import Client
# from django.http import HttpResponse

# from SentDex
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def home(request):
 return render(request,'home.html')

def register(request):
 if request.method == 'POST':
  a = request.POST.get('name')
  b = request.POST.get('age')
  c = request.POST.get('weight')
  d = request.POST.get('height')
  e = request.POST.get('address')
  f = request.POST.get('joinDate')
  g = request.POST.get('membership')
  instance_ = Client(clientName=a,clientAge=b,clientWeight=c,clientHeight=d,\
   clientAddress=e,clientJoinDate=f,clientPlan=g)
  instance_.save()

 return render(request,'register.html')

def member(request):
 table_ = Client.objects.all()
 return render(request,'members.html',{'tableData' : table_})

def membership(request):
 return render(request,'memberships.html')

def addEmployee(request):
 eform = Employee()

def aform(request):
 
 if request.method == 'POST':
  bform = UserCreationForm(request.POST)
  if bform.is_valid():
   user = bform.save()
   login(request,user)
   return redirect('myApp : home')
  else:
   for msg in bform.error_messages:
    print(bform.error_messages[msg])

 eform = UserCreationForm
 return render(request,'aform.html',context={"form":eform})
 