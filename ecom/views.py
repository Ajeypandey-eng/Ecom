from django.shortcuts import render,redirect,HttpResponse
from .models import *
# Create your views here.

def show(request):
    data = Student.objects.all()
    print(data)
    # for i in data:
    #     print(i.email)
    return render(request,'show.html',{'student':data})

def showimg(request):
    dataimg = Img.objects.all()
    return render(request,'showimg.html',{'dataimg':dataimg})


def store(request):
    if request.method == 'POST':
        print("this is first line after post method ")
        store_data = Student()
        store_data.email = request.POST['email']
        store_data.name = request.POST['uname']
        store_data.save()
    return render(request,'store.html')


def storeget(request):
    if request.method == 'GET':
        # store_data = Student()
        email = request.GET.get('email')
        name = request.GET.get('uname')
        # store_data.save()
        print(name,email)
    return render(request,'storeget.html')


def storeimg(request):
    if request.method == 'POST' and request.FILES:
        store_image = Img()
        store_image.name = request.POST['name']
        store_image.image = request.FILES['image']
        store_image.save()
    return render(request,'storeimg.html')

def register(request):
    if request.method == 'POST':
        sign_up = Registration(email = request.POST['email'],
                               name = request.POST['name'],
                               mob = request.POST['mob'],
                               add = request.POST['add'],
                               password = request.POST['password'])
        try:
            already_reg = Registration.objects.get(email = request.POST['email'])
            if already_reg:
                return render(request,'register.html',{'already':"Email already exists.."})   
        except:
            sign_up.save()
            # return render(request,'register.html',{'registration':"Registration successfull."})
            return redirect('login')
    else:
        return render(request,'register.html')
    
def login(request):
    if request.method == 'POST':
        try:
            is_present = Registration.objects.get(email = request.POST['email'])
            if is_present:
                if request.POST['password'] == is_present.password:
                    request.session['login'] = is_present.email
                    return redirect('index')
                else:
                    return render(request,'login.html',{'wrong_pass':"password is incorrect..."})
        except:
            return render(request,'login.html',{'not_registered':"this email does not exists..."})
    else:
        return render(request,'login.html')
    
def profile(request):
        if 'login' in request.session:
            logged_user = Registration.objects.get(email = request.session['login'])
            if request.method == 'POST':
                # update_user = logged_user(name = request.POST['name'],
                #             mob = request.POST['mob'],
                #             add = request.POST['add']  )
                logged_user.name = request.POST['name']
                logged_user.add = request.POST['add']
                logged_user.mob = request.POST['mob']
                logged_user.save()
                # return render(request,'profile.html',{'logged_in':True,'logged_user':logged_user})
                return redirect('profile')
            else:
                return render(request,'profile.html',{'logged_in':True,'logged_user':logged_user})
        else:
            return redirect('login')
    # else:
    #     return redirect('login')

def index(request):
    cat = category.objects.all()
    if 'login' in request.session:
        return render(request,'index.html',{'cat':cat,'logged_in':True})
    else:
        return render(request,'index.html',{'cat':cat})


def logout(request):
    del request.session['login']
    return redirect('index')

def cat_pro(request,id):
    pro = Product.objects.filter(category = id)
    if 'login' in request.session:
        return render(request,'cat_pro.html',{'pro':pro,'logged_in':True})
    else:
        return render(request,'cat_pro.html',{'pro':pro})


def pro_details(request,id):
    prod = Product.objects.get(pk = id)
    if 'login' in request.session:
        logged_in = Registration.objects.get(email = request.session['login'])
        # if request.method == 'POST':
        if 'buy' in request.POST:
            if int(request.POST['qty']) > prod.stock:
                return render(request,'product.html',{'logged_in':True,'product':prod,'less_stock':True})
            else:
                request.session['qty'] = request.POST['qty']
                request.session['proid'] =  id
                return redirect('checkout')
        elif 'cart' in request.POST:
            add_to_cart = Cart(user = logged_in,
                 pro = prod,
                 qty = request.POST['qty'],
                 total_price = prod.price * int(request.POST['qty'])
                 )
            add_to_cart.save()
            return render(request,'product.html',{'logged_in':True,'product':prod})
        else:
            return render(request,'product.html',{'logged_in':True,'product':prod})
    else:
        return render(request,'product.html',{'product':prod})


def cart_view(request):
    if 'login' in request.session:
        logged_in = Registration.objects.get(email = request.session['login'])
        cart_data = Cart.objects.filter(user = logged_in,order_id = 0)
        total = 0
        for i in cart_data:
            total += i.total_price
        return render(request,'cart.html',{'logged_in':True,'cart':cart_data,'total':total})
    else:
        return redirect('login')
    
def pro_details(request,id):
    prod = Product.objects.get(pk = id)
    if 'login' in request.session:
        logged_in = Registration.objects.get(email = request.session['login'])
        # if request.method == 'POST':
        if 'buy' in request.POST:
            if int(request.POST['qty']) > prod.stock:
                return render(request,'product.html',{'logged_in':True,'product':prod,'less_stock':True})
            else:
                request.session['qty'] = request.POST['qty']
                request.session['proid'] =  id
                return redirect('checkout')
        elif 'cart' in request.POST:
            add_to_cart = Cart(user = logged_in,
                 pro = prod,
                 qty = request.POST['qty'],
                 total_price = prod.price * int(request.POST['qty'])
                 )
            add_to_cart.save()
            return render(request,'product.html',{'logged_in':True,'product':prod})
        else:
            return render(request,'product.html',{'logged_in':True,'product':prod})
    else:
        return render(request,'product.html',{'product':prod})
