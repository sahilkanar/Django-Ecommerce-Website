from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .models import *
from .forms import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    c = Category.objects.all()
    p = Products.objects.all() 
    return render(request,'home.html',{'product':p,'cat':c})


def user_login(request):
    if request.method=='POST':
        fm=Loginform()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.add_message(request,messages.SUCCESS,'Login Successful')
            return redirect('login')
        
        else:
            messages.add_message(request,messages.ERROR,'Invalid Credentials')
    fm=Loginform()
    return render(request,'login.html',{'forms':fm})

def user_logout(request):
    logout(request)
    messages.add_message(request,messages.SUCCESS,'Logged Out Successfully')
    return redirect('home')

def user_register(request):
    if request.method=='POST':
        fm=Registrationform(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,'Registration Successful')
    fm=Registrationform()
    return render(request,'register.html',{'forms':fm})


def user_update(request):
    pi=User.objects.get(id=request.user.id)
    if request.method=='POST':
        fm=Updateform(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    fm=Updateform(instance=pi)
    return render(request,'updateprofile.html',{'forms':fm})

def view_product(request,id):
    fm=Products.objects.filter(id=id)
    f = Rating.objects.filter(product_id=id)
    return render(request,'viewproduct.html',{'forms':fm,'review':f})

@login_required(login_url='login')
def rating(request,id):
    prod = Products.objects.get(id=id)
    if request.method=='POST':
        rate = request.POST['stars']
        review = request.POST['review']
        fm = Rating(user=request.user,product=prod,review=review,rating=rate)
        fm.save()
        return render(request,'viewproduct.html')
    return render(request,'viewproduct.html')

@login_required(login_url='login')
def cart(request,id):
    prod = Products.objects.get(id=id)
    create_item,item_created=Cart.objects.get_or_create(user=request.user,cart=prod)
    if not item_created:
        create_item.quantity += 1
        create_item.save()
    
    return redirect('home')


def search(request):
    pass

@login_required(login_url='login')
def viewcart(request):
    fm=Cart.objects.filter(user=request.user)
    total=0
    quantity=0
    for i in fm:
        subtotal=i.quantity*i.cart.price
        total = total+subtotal
        quantity=quantity+i.quantity
    return render(request,'cart.html',{'forms':fm,'total':total,'quantity':quantity})


def increase_cart(request,id):
    product=Products.objects.get(id=id)
    cart_item,item_created=Cart.objects.get_or_create(user=request.user,cart=product)
    cart_item.quantity+=1
    cart_item.save()
    return redirect('viewcart')



def decrease_cart(request,id):
    product=Products.objects.get(id=id)
    cart_item,item_created=Cart.objects.get_or_create(user=request.user,cart=product)
    cart_item.quantity-=1
    cart_item.save()

    cart_data=Cart.objects.filter(quantity=0)
    cart_data.delete()
    return redirect('viewcart')


def remove_cart(request,id):
    fm=Cart.objects.filter(id=id)
    fm.delete()
    return redirect('viewcart')


def category(request,id):
    fm=Products.objects.filter(category_id=id)
    return render(request,'category.html',{'forms':fm})


def search(request):
    if request.method=='POST':
        value=request.POST['data']
        fm = Products.objects.filter(title__contains=value)
        return render(request,'search.html',{'forms':fm})
    


def checkout(request):
    cart_info=Cart.objects.filter(user=request.user)
    total=0
    quantity=0
    for i in cart_info:
        subtotal=i.quantity*i.cart.price
        total=total+subtotal
        quantity=quantity+i.quantity
        p_id=i.cart


        if request.method=='POST':
            fname=request.POST['fname']
            email=request.POST['email']
            mobile=request.POST['mobile']
            address=request.POST['address']
            order = Orders.objects.create(user=request.user,product=p_id,quantity=quantity,address=address,total_amount=total,fname=fname,mobile_no=mobile,email=email)
            order.save()
            cart = Cart.objects.filter(user=request.user)
            cart.delete()
            messages.add_message(request,messages.SUCCESS,'Order Placed Successfully')
            return redirect('home')
    return render(request,'checkout.html',{'total':total})


def order(request):
    orders = Orders.objects.filter(user=request.user)
    return render(request,'orders.html',{'orders':orders})