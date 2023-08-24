from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import *
# Create your views here.

def data(request):
    return HttpResponse('<h1>this is my first webpage<h1>')

def login(request):
    if request.method=="POST":
        email1=request.POST['email']
        password1=request.POST['password']
        try:
            user=Userregister.objects.get(email=email1,password=password1)
            if user:
                request.session['email']=user.email
                request.session['id']=user.pk
                request.session['name']=user.name
                return redirect('index')
            else:
                return render(request,'login.html',{'m':"invalid email and password"})
        except:
            return render(request,'login.html',{'m':"invalid email and password"})
    return render(request,'login.html')

def register(request):
    if request.method=="POST":
        name1=request.POST['name']
        email1=request.POST['email']
        number1=request.POST['number']
        address1=request.POST['address']
        pass1=request.POST['password']
        # print(name1,pass1)
        user=Userregister(name=name1,email=email1,number=number1,address=address1,password=pass1)
        # data=Userregister.objects.filter(email=email1).exists()
        data=Userregister.objects.filter(email=email1)
        if len(data) == 0:
            user.save()
            return redirect('login')
        else:
            return render(request,'register.html',{'m':'user already exist'})
    return render(request,'register.html')
def logout(request):
    if 'email' in request.session:
        del request.session['email']
        del request.session['id']
        del request.session['name']
        return redirect('login')
    else:
        return redirect('login')


def profile(request):
    if 'email' in request.session:
        user=Userregister.objects.get(email=request.session['email'])
        if request.method=="POST":
            user.name=request.POST['name']
            user.number=request.POST['number']
            user.address=request.POST['address']
            user.save()
            request.session['name']=request.POST['name']
            return render(request,'profile.html',{'data':user,'m':"profile updated"})
        return render(request,'profile.html',{'data':user})
    else:
        return redirect('login')

def index(request):
    a=Category.objects.all()
    return render(request,'index.html',{'data':a})

def allproduct(request):
    a=Product.objects.all()
    return render(request,'product.html',{'data':a})


def filterproduct(request,id):
    a=Product.objects.filter(categoryname=id)
    return render(request,'product.html',{'data':a})

def productget(request,id):
    if 'm' in request.session:
        m=request.session['m']
        del request.session['m']
    else:
        m=""
    productdata=Product.objects.get(id=id)
    return render(request,'product_details.html',{'data':productdata,'m':m})



def Sellerregister(request):
    if request.method=="POST":
        name1=request.POST['name']
        email1=request.POST['email']
        number1=request.POST['number']
        address1=request.POST['address']
        pass1=request.POST['password']
        # print(name1,pass1)
        user=sellerregister(name=name1,email=email1,number=number1,address=address1,password=pass1)
        # data=Userregister.objects.filter(email=email1).exists()
        data=sellerregister.objects.filter(email=email1)
        if len(data) == 0:
            user.save()
            return redirect('slogin')
        else:
            return render(request,'register.html',{'m':'user already exist'})
    return render(request,'register.html')

def sellerlogin(request):
    if request.method=="POST":
        email1=request.POST['email']
        password1=request.POST['password']
        try:
            user=sellerregister.objects.get(email=email1,password=password1)
            if user:
                request.session['semail']=user.email
                request.session['sid']=user.pk
                request.session['sname']=user.name
                return redirect('index')
            else:
                return render(request,'login.html',{'m':"invalid email and password"})
        except:
            return render(request,'login.html',{'m':"invalid email and password"})
    return render(request,'login.html')

def sellerlogout(request):
    if 'semail' in request.session:
        del request.session['semail']
        del request.session['sid']
        del request.session['sname']
        return redirect('slogin')
    else:
        return redirect('slogin')
    
def addproduct(request):
    if 'semail' in request.session:
        a=Category.objects.all()
        if request.method=="POST" and request.FILES:
            pro=Product()
            pro.vendorid=request.session['sid']
            b=Category.objects.get(id=request.POST['category'])
            pro.categoryname=b
            pro.name=request.POST['name']
            pro.price=request.POST['price']
            pro.quantity=request.POST['quantity']
            pro.discription=request.POST['desc']
            pro.image=request.FILES['img']
            pro.save()
        return render(request,'addproduct.html',{'data':a})
    else:
        return redirect('slogin')


def addcart(request):
    if 'email' in request.session:
        try:
            if request.POST:
                data=Cart()
                data.userid=request.session['id']
                data.productid=request.POST['productid']
                x=request.POST['productid']
                a=Product.objects.get(id=x)
                data.vendorid=a.vendorid
                data.quantity=request.POST['quantity']
                data.totalprice=a.price*int(data.quantity)
                z=Cart.objects.filter(productid=x) and Cart.objects.filter(userid=request.session['id']) and Cart.objects.filter(orderid="0")
                if len(z)==0:
                    data.save()
                    request.session['m']="product added"
                    return redirect('proget1',x)
                else:
                    request.session['m']="product already into cart"
                    return redirect('proget1',x)
        except:
                request.session['m']="Enter valid Quantity"
                return redirect('proget1',x)
    else:
        return redirect('login')
    

def viewcart(request):
    if 'email' in request.session:
        data=Cart.objects.filter(userid=request.session['id']) and Cart.objects.filter(orderid="0")
        xy=[]
        final=0
        for i in data:
            final+=int(i.totalprice)
            d={}
            productdata=Product.objects.get(id=i.productid)
            d['name']=productdata.name
            d['id']=i.pk
            d['img']=productdata.image
            d['price']=productdata.price
            d['quantity']=i.quantity
            d['totalprice']=i.totalprice
            xy.append(d)
        return render(request,'cart.html',{'prolist':xy,'noitem':len(xy),'final':final})
    else:
        return redirect('login')


def removeitem(request,id):
    if 'email' in request.session:
        a=Cart.objects.get(id=id)
        a.delete()
        return redirect('view_cart')
    else:
        return redirect('login')

def removeallitem(request):
    if 'email' in request.session:
        a=Cart.objects.filter(userid=request.session['id']) and Cart.objects.filter(orderid="0") 
        a.delete()
        return redirect('view_cart')
    else:
        return redirect('login')
    
def shipping(request):
    if 'email' in request.session:
        userdata=Userregister.objects.get(id=request.session['id'])
        data=Cart.objects.filter(userid=request.session['id']) and Cart.objects.filter(orderid="0")
        final=0
        for i in data:
            final+=int(i.totalprice)
        if request.method=="POST":
            request.session['name']=request.POST['name']
            request.session['number']=request.POST['number']
            request.session['address']=request.POST['address']
            request.session['price']=request.POST['final']
            request.session['paymentmethod']="Razorpay"
            return redirect('razorpayView')

           
        return render(request,'shipping.html',{'user':userdata,'final':final})
    else:
        return redirect('login')

def success(request):
    if 'email' in request.session:
         return render(request,'success.html')
    else:
        return redirect('login')


import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest


RAZOR_KEY_ID = 'rzp_test_D2CSJ2vNEiyjL7'
RAZOR_KEY_SECRET = '0j3Gr9p35rAGYRVz4pBFYBG4'
client = razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))

def razorpayView(request):
    currency = 'INR'
    amount = int(request.session['price'])*100
    # Create a Razorpay Order
    razorpay_order = client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'http://127.0.0.1:8000/paymenthandler/'    
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url    
    return render(request,'razorpayDemo.html',context=context)

@csrf_exempt
def paymenthandler(request):
    # only accept POST request.
    if request.method == "POST":
        try:
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')

            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = client.utility.verify_payment_signature(
                params_dict)
            
            amount = int(request.session['price'])*100  # Rs. 200
            # capture the payemt
            client.payment.capture(payment_id, amount)

            #Order Save Code
            orderModel = Order()
            orderModel.userid=request.session['id']
            orderModel.name=request.session['name']
            orderModel.email=request.session['email']
            orderModel.number=request.session['number']
            orderModel.address=request.session['address']
            orderModel.price = request.session['price']
            orderModel.paymentmethod = request.session['paymentmethod']
            orderModel.transactionid = payment_id
            orderModel.save()
            orderdata=Order.objects.latest('id')
            data=Cart.objects.filter(userid=request.session['id']) and Cart.objects.filter(orderid="0")
            for i in data:
                productdata=Product.objects.get(id=i.productid)
                productdata.quantity-=int(i.quantity)
                # productdata.quantity=productdata.quantity-int(i.quantity)
                productdata.save()
                i.orderid=orderdata.pk
                i.save()
            del request.session['name']
            del request.session['number']
            del request.session['address']
            del request.session['price']
            del request.session['paymentmethod']
        
            return redirect('success123')
            
        except:
            
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       
       # if other than POST request is made.
        return HttpResponseBadRequest()

def ordertable(request):
    if 'email' in request.session:
        orderdata=Order.objects.filter(userid=request.session['id']).order_by('-id')
        return render(request,'ordertable.html',{'orderdata':orderdata})
    else:
        return redirect('login')