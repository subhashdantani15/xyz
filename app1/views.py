from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import *
# Create your views here.


def data(request):
    return HttpResponse("<h1>This is my first webpage</h1>")


def index(request):
    a=Category.objects.all()
    return render(request,'index.html',{'data':a})

def productall(request):
    if 'Vendoremail' in request.session:
        a=Product.objects.filter(vendorid=request.session['Vendorid'])
        return render(request,'product.html',{'data':a})
    else:
        a=Product.objects.all()
        return render(request,'product.html',{'data':a})

def productfilter(request,id):
    a=Product.objects.filter(Category=id)
    return render(request,'product.html',{'data':a})

from django.db.models import Q

def productsearch(request):
    word=request.GET.get('search')
    worddata=word.split(" ")
    print(worddata)
    for i in worddata:
        a=Product.objects.filter(Q(Category__categoryname__icontains=i)|Q(name__icontains=i)|Q(price__icontains=i)).distinct()
    return render(request,'product.html'    ,{'data':a})

def productget(request,id):
    if 'm' in request.session:
        m=request.session['m']
        del request.session['m']
    else:
        m=""
    a=Product.objects.get(id=id)
    return render(request,'product_details.html',{'a':a,'m':m})

def login(request):
    if request.method=="POST":
        email1=request.POST['email']
        pass1=request.POST['password']
        try:
            user=Userregister.objects.get(email=email1,password=pass1)
            if user:
                request.session['email']=user.email
                request.session['id']=user.pk
                return redirect('home')
            else:
                return render(request,'login.html',{'m':"invalid userid and password"})
        except:
            return render(request,'login.html',{'m':"invalid data enter"})
    return render(request,'login.html')

def logout(request):
    if 'email' in request.session:
        del request.session['email']
        del request.session['id']
        return redirect('login1')
    else:
        return redirect('login1')

def register(request):
    if request.method=="POST":
        name1=request.POST['name']
        email1=request.POST['email']
        number1=request.POST['number']
        address1=request.POST['address']
        pass1=request.POST['pswd']
        user=Userregister(name=name1,email=email1,number=number1,address=address1,password=pass1)
        print(Userregister.objects.filter(email=email1).exists())
        if len(Userregister.objects.filter(email=email1)) ==0:
            user.save()
        else:
            return render(request,'register.html',{'m':"user alredy exist"})
    return render(request,'register.html')


def profile(request):
    if 'email' in request.session:
        userdata=Userregister.objects.get(email=request.session['email'])
        if request.method=="POST":
            userdata.name=request.POST['name']
            userdata.number=request.POST['number']
            userdata.address=request.POST['address']
            userdata.save()
            return render(request,'profile.html',{'user':userdata,'m':'profile updated'})
        return render(request,'profile.html',{'user':userdata})
    else:
        return redirect('login1')
    

def changepass(request):
    if 'email' in request.session:
        userdata=Userregister.objects.get(email=request.session['email'])
        if request.method=="POST":
            old=request.POST['oldpass']
            newpass=request.POST['password']
            c_pass=request.POST['cpassword']
            if userdata.password==old:
                if newpass==c_pass:
                    userdata.password=newpass
                    userdata.save()
                    return render(request,'changepass.html',{'user':userdata,'m':'Password Updated..'})
                else:
                    return render(request,'changepass.html',{'user':userdata,'m':'Password Missmatch'})
            else:
                return render(request,'changepass.html',{'user':userdata,'m':'Incorrect Old Password'})

        return render(request,'changepass.html',{'user':userdata})
    else:
        return redirect('login1')
    

''' vendor login-register-logout'''


def vendorlogin(request):
    if request.method=="POST":
        email1=request.POST['email']
        pass1=request.POST['password']
        try:
            Vendor=Vendorregister.objects.get(email=email1,password=pass1)
            if Vendor:
                request.session['Vendoremail']=Vendor.email
                request.session['Vendorid']=Vendor.pk
                return redirect('home')
            else:
                return render(request,'login.html',{'m':"invalid userid and password"})
        except:
            return render(request,'login.html',{'m':"invalid data enter"})
    return render(request,'login.html')

def vendorlogout(request):
    if 'Vendoremail' in request.session:
        del request.session['Vendoremail']
        del request.session['Vendorid']
        return redirect('Vendorlogin')
    else:
        return redirect('Vendorlogin')

def vendorregister(request):
    if request.method=="POST":
        name1=request.POST['name']
        email1=request.POST['email']
        number1=request.POST['number']
        address1=request.POST['address']
        pass1=request.POST['pswd']
        Vendor=Vendorregister(name=name1,email=email1,number=number1,address=address1,password=pass1)
        
        if len(Vendorregister.objects.filter(email=email1)) ==0:
            Vendor.save()
            return redirect('Vendorlogin')
        else:
            return render(request,'register.html',{'m':"Vendor alredy exist"})
    return render(request,'register.html')

def add_product(request):
    if 'Vendoremail' in request.session:
        a=Category.objects.all()
        if request.method=="POST" and request.FILES['img']:
            pro=Product()
            b=Category.objects.get(id=request.POST['category'])
            pro.vendorid=request.session['Vendorid']
            pro.Category=b
            pro.name=request.POST['name']
            pro.quantity=request.POST['quantity']
            pro.description=request.POST['disc']
            pro.img=request.FILES['img']
            pro.price=request.POST['price']
            pro.save()
        return render(request,'addproduct.html',{'data':a})
    else:
        return redirect('Vendorlogin')
    
def updateproduct(request,id):
    if 'Vendoremail' in request.session:
        a=Product.objects.get(id=id)
        b=Category.objects.all()
        
        return render(request,'updateproduct.html',{'a':a,'data':b})
    else:
        return redirect('Vendorlogin')
    

def addcart(request):
    if 'email' in request.session:
        if request.POST:
            try:
                data=Cart()
                data.userid=request.session['id']
                data.productid=request.POST['productid']
                x=request.POST['productid']
                a=Product.objects.get(id=x)
                data.vendorid=a.vendorid
                data.orderid="0"
                data.quantity=request.POST['quantity']
                data.totalprice=a.price*int(data.quantity)
                a=Cart.objects.filter(productid=x)
                if len(a)==0:
                    data.save()
                    request.session['m']="product added"
                    return redirect('product_get',x)
                else:
                    request.session['m']="product already exists"
                    return redirect('product_get',x)
            except:
                request.session['m']="enter the valid quantity"
                return redirect('product_get',x)

    else:
        return redirect('login1')
    

def cartpage(request):
    if 'email' in request.session:
        data=Cart.objects.filter(userid=request.session['id']) and Cart.objects.filter(orderid="0")
        d=[]
        final=0
        for i in data:
            final+=int(i.totalprice)
            prodict={}
            prodata=Product.objects.get(id=i.productid)
            prodict['name']=prodata.name
            prodict['id']=i.pk
            prodict['img']=prodata.img
            prodict['price']=prodata.price
            prodict['quantity']=i.quantity
            prodict['totalprice']=i.totalprice
            d.append(prodict)

        return render(request,'cart.html',{'prolist':d,'final':final,'noitem':len(d)})
    else:
        return redirect('login1')
    

def removeitem(request,id):
    if 'email' in request.session:
        data=Cart.objects.get(id=id)
        data.delete()
        return redirect('cart2')
    else:
        return redirect('login1')

def removeallitem(request):
    if 'email' in request.session:
        data=Cart.objects.filter(userid=request.session['id']) and Cart.objects.filter(orderid="0")
        data.delete()
        return redirect('cart2')
    else:
        return redirect('login1')
    
def shiping(request):
    if 'email' in request.session:
        userdata=Userregister.objects.get(id=request.session['id'])
        data=Cart.objects.filter(userid=request.session['id']) and Cart.objects.filter(orderid="0")
        final=0
        for i in data:
            final+=int(i.totalprice)
        if request.POST:
        
            request.session['name']=request.POST['name']
            request.session['email']=request.POST['email']
            request.session['number']=request.POST['number']
            request.session['address']=request.POST['address']
            request.session['price']=request.POST['final']
            request.session['paymentmethod']="Razorpay"
            return redirect('razorpayView')


            # myorder=Order.objects.latest('id')
            # for j in data:
            #     j.orderid=myorder.pk
            #     j.save()
            # return redirect('success1')
        return render(request,'shipping.html',{'final':final,'userdata':userdata})
    else:
        return redirect('login1')
    
def success(request):
    if 'email' in request.session:
        return render(request,'success.html')
    else:
        return redirect('login1')



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
            orderModel.totalprice = request.session['price']
            orderModel.paymentmethod = request.session['paymentmethod']
            orderModel.transactionid = payment_id
            orderModel.save()
            orderdata=Order.objects.latest('id')
            data=Cart.objects.filter(userid=request.session['id']) and Cart.objects.filter(orderid="0")
            for i in data:
                productdata=Product.objects.get(id=i.productid)
                productdata.quantity-=int(i.quantity)
                productdata.save()
                i.orderid=orderdata.pk
                i.save()
            del request.session['name']
            del request.session['number']
            del request.session['address']
            del request.session['price']
            del request.session['paymentmethod']
        
            return redirect('success1')
            
        except:
            print("Hello")
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
        print("Hello1")
       # if other than POST request is made.
        return HttpResponseBadRequest()


def ordertable(request):
    if 'email' in request.session:
        myorder=Order.objects.filter(userid=request.session['id'])

        return render(request,'ordertable.html',{'myorder':myorder})
    else:
        return redirect('login1')

def orderdetails(request,id):
    if 'email' in request.session:
        myorder=Order.objects.get(id=id)
        cartdata=Cart.objects.filter(orderid=myorder.pk)
        d=[]
        final=0
        for i in cartdata:
            prodict={}
            prodata=Product.objects.get(id=i.productid)
            prodict['name']=prodata.name
            prodict['img']=prodata.img
            prodict['dis']=prodata.description
            prodict['quantity']=i.quantity
            prodict['totalprice']=i.totalprice
            d.append(prodict)



        return render(request,'orderdetails.html',{'myorder':myorder,'prolist':d})
    else:
        return redirect('login1') 


def vendor_order(request):
    if 'Vendoremail' in request.session:
        myorder=Cart.objects.filter(vendorid=request.session['Vendorid'])
        d=[]
        for i in myorder:
            if i.orderid != "0":
                prodict={}
                prodata=Product.objects.get(id=i.productid)
                orederdata=Order.objects.get(id=i.orderid)
                userdata=Userregister.objects.get(id=i.userid).name
                prodict['name']=prodata.name
                prodict['img']=prodata.img
                prodict['transactionid']=orederdata.transactionid
                prodict['date']=orederdata.datetime
                prodict['user']=userdata
                prodict['quantity']=i.quantity
                prodict['totalprice']=i.totalprice
                d.append(prodict)            
        return render(request,'vendororder.html',{'prolist':d})
    else:
        return redirect('Vendorlogin')