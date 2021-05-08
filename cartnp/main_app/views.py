from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from main_app.models import product_info1, userregistration1
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.


def homepage(request):

    my_dict=product_info1.objects.all()
    return render(request,'index.html',{'my_dict':my_dict})


    # Search

def search(request):
    if request.method=='GET':
        query=request.GET['query']
        
        if not query:
            return redirect('home')


    my_dict1= product_info1.objects.filter(product_name__icontains=query)

    return render(request,'search.html',{'my_dict1':my_dict1})

    

    # Login


def login(request):

    if request.method=="POST":
        username=request.POST['uname']
        password=request.POST['psw']

        user_c=auth.authenticate(username=username,password=password)

        if user_c is not None:
            auth.login(request,user_c)
            messages.success(request,'Succesfully Logged in')
            return redirect('home')
        else:
            messages.error(request,'Invalid Credintials')
            return redirect('login')

    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def sell(request):
    if request.method=='POST':
        product_name=request.POST['product_name']
        product_price=request.POST['product_price']
        product_des=request.POST['product_des']
        product_contact=request.POST['product_contact']
        product_image=request.FILES['product_image']

        new_instance=product_info1(product_name=product_name,product_price=product_price,product_des=product_des,product_contact=product_contact,product_image=product_image)
        new_instance.save()
        return redirect('/')



    return render(request,'sell.html')

def signup(request):

    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password =request.POST['password']
        retype_password=request.POST['retype_password']

        my_user=User.objects.create_user(username=username,email=email,password=password)
        my_user.save()
        messages.success(request,'Succesfuly Created User')
        return redirect('login')
   
         

    return render(request,'signup.html')