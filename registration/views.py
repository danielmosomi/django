from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from registration.models import client


def registration(request):
    return HttpResponse("Welcome to registration")

def login(request):
    template=loader.get_template('login.html')
    return HttpResponse(template.render())
def register(request):
    template=loader.get_template('About us.html')
    return HttpResponse(template.render())
def home(request):
    template=loader.get_template('home.html')
    return HttpResponse(template.render())

def myregister(request):
    template=loader.get_template('register.html')
    return HttpResponse(template.render())

def dashboard(request):
    template=loader.get_template('dashboard.html')
    return HttpResponse(template.render())

@csrf_exempt
def addregister(request):
    if request.method =='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm=request.POST.get('confirm password')



        obj1=client(username=username, email=email, password=password, confirm_password=confirm)
        obj1.save()
        data=client.objects.all()
        context={'data':data}
        return render(request,'register.html',context)



# Create your views here.
