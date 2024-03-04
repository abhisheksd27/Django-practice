from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import features
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def index(request):
    
    # #name ="Abhishek"
    # context = {
    #     'name':"Abhishek",
    #     'age': 21,
    #     'nationality':"Indian",
    # }
    # # return render(request,'index.html',{'name': name})
    # return render(request,'index.html',context)
    # feature1=features()
    # feature1.id = 0
    # feature1.name ='Fast'
    # feature1.is_true = True
    # feature1.details ='A kjdiuv ihcv  jhwifueviwuhifvuehqwiuvec'

    # feature2=features()
    # feature2.id = 1
    # feature2.name ='slow'
    # feature2.is_true = True
    # feature2.details ='B vdljiuhbv iidv wefjwnaicnwkjvc'

    # feature3=features()
    # feature3.id = 2
    # feature3.name ='Fast-slow'
    # feature3.is_true = False
    # feature3.details ='C vdsjhviuhv ewvvmniwhevuiwwwwfefw'

    # feature4=features()
    # feature4.id = 3
    # feature4.name ='slow-Fast'
    # feature4.is_true = True
    # feature4.details ='Dvnvishdi yevwshiuvwkjnw ihwifehiqwu'

   

    # feature =[feature1,feature2,feature3,feature4]
    
    
    # return render(request,'index.html',{'feature': feature1,'feature2':feature2 ,'feature3':feature3 ,'feature4':feature4 })
    feature =features.objects.all()
    return render(request,'index.html',{'features': feature})

# def counter(request):
#     words = request.POST['words']# textarea name is words
#     count=len(words)
#     # count=len(words.split())

#     return render(request,'counter.html',{'count':count})


def register(request):

    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, ' Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username is already taken')
                return redirect('register')
            
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, ' password not matched')
            return redirect('register')
    else:
        return render(request,'register.html')
    

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials Invalid')
            return redirect('login')
    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

#dynamic url routing in django
def post(request,pk):
    return render(request,'post.html',{'pk':pk})

def counter(request):
    posts=[1,2,3,4,5,"tim","tom","john"]
    return render(request,'counter.html',{'posts':posts})