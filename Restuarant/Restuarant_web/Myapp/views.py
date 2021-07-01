from django import forms
from django.shortcuts import redirect, render
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib import messages 

# Create your views here.

#---------------signin or signup--------------------------------------

def signin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['Username']
        loginpassword=request.POST['password']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request,user)
            return redirect("index")
        else:
            return redirect("signin")
    return render(request,'Myapp/signin.html')

def logouts(request):
    logout(request)
    return temp(request)

def signup(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['Username']
        email=request.POST['Email']
        fname=request.POST['Fname']
        lname=request.POST['Lname']
        pass1=request.POST['Password']
        pass2=request.POST['Confirm Password']

        # check for passwords if matching ot not 
        if (pass1!= pass2):
            messages.error(request, " Passwords do not match")
            return redirect('signup')
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your Royal Kitchen account has been successfully created")
        return redirect('signin')
    return render(request,'Myapp/signup.html')

#------------end cart-----------------------------------------------

def temp(request):
    offerset = Offers.objects.all()
    dataset = Customer.objects.all()
    foodset = Product.objects.all()
    ######################################
    webset =  WebResources.objects.all()
    max=WebResources.objects.count()
    if(max!=0):
        max=1
    obj=WebResources.objects.get(pk=max)
    ######################################
    ceoset = CEO.objects.all()
    contactform = contactusform()
    if request.method == 'POST':
        contactform = contactusform(request.POST)
        if contactform.is_valid:
            contactform.save()
    return render(request,'Myapp/index.html',{'dat':dataset,'offers':offerset,'product':foodset,'form':contactform,'max':obj,'webset':webset,'ceo':ceoset})

def savecustomer(request):
    form = cusform()
    if request.method == 'POST':
        form = cusform(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/customers')
    context ={'form':form}
    return render(request,'Myapp/Customerform.html',context)

def updatecustomer(request,pk):
    form1= Customer.objects.get(id=pk)
    form=cusform(instance=form1)
    if request.method == 'POST':
        form = cusform(request.POST,instance=form1)
        if form.is_valid:
            form.save()
           # return redirect('/customers')
    context ={'form':form1}
    return render(request,'Myapp/updatecustomer.html',context)

def deletecustomer(request,pk):
    form1= Customer.objects.get(id=pk)
    form1.delete()
    return redirect('index')


#add to cart_view
@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return temp(request)

@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")

@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")

@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")

@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")

@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'Myapp/cart.html')


#----------cart view----------------
@login_required(login_url="/users/login")
def store(request):
    total=0.00
    cart = Cart(request)
    ab=request.session['cart']
    print(ab)

    for key,value in ab.items():
        print(value['name'])
        total = float( float(value['price'])* float(value['quantity'])) + float(total)
    print(total) 
    print(request.user)

    obj=Req_info(Name_Costomer=request.user,GrandTotal=total)
    obj.save()

    print(value['userid'])
    max_val=Req_info.objects.latest('id')
   # print(max_val)
    for key,value in ab.items():
        print(value['name'])   
        OrdereProduct.objects.create(order=max_val,  CustomerID=value['userid'], Name_Costomer=request.user,  name=value['name'], quantity=value['quantity'], price=value['price'])
    cart.clear()
    return temp(request) #render(request, 'Myapp/index.html', {'cart': cart})
#----------end cart------------------