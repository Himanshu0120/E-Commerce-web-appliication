from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from .models import product,category,customer
from .models import orders
from django.contrib.auth.hashers import make_password,check_password
from .middlewares.auth import auth_middleware

# Create your views here.
def home(request):
    
    if request.method=='GET':
        if not request.session.get('cart'):
            request.session['cart']={}
        products=product.Product.get_all_products()
        category_r=request.GET.get('category')
        if category_r ==0:
            products=product.Product.get_all_products()
        else:
            products=product.Product.get_products_byId(category_r)
        
        categories=category.Category.get_all_categories()
        return render(request,'store/home.htm',{'prds':products,'cat':categories})
    else:
        if request.POST.get('remove'):
            id= request.POST.get('remove')
            cart=request.session.get('cart')
            q=cart[id]
            if q<=1:
                cart.pop(id)
            else:
                cart[id]=q-1
            
        else:
            print('getting add')
            id=request.POST.get('id')
            cart=request.session.get('cart')
            if cart:
                quantity=cart.get(id)
                if quantity:
                    cart[id]=quantity+1
                else:
                    cart[id]=1
                    
            else:
                cart={}
                cart[id]=1
            
        request.session['cart']=cart   
        return redirect('homepage')

def signup(request):
    
    if request.method=='GET':
        return render(request,'store/signup.htm')
    else:
        data=request.POST
        first=data.get('first_name')
        last=data.get('last_name')
        phone=data.get('phone')
        email=data.get('email')
        password=make_password(data.get('password'))


        ob=customer.Customer(first_name=first,last_name=last,phone=phone,email=email,password=password)
        ob.save()
        return redirect('homepage')

def login(request):
    
    if request.method=='GET':
        request.session['url']=request.GET.get('return_url')
        print('redirected from checkout')
        print('return to',request.GET.get('return_url'))
        return render(request,'store/login.htm')
    else:
        email=request.POST.get('email')
        password=request.POST.get('password')
        error_message=None
        cus=customer.Customer.get_customer_by_id(email)
        
        if not cus:
            error_message='Wrong email id'
            
        else :
            if check_password(password,cus[0].password):
                request.session['customer_id']=cus[0].id
                request.session['email']=cus[0].email
                if not request.session.get('url'):
                   
                    return redirect('homepage')
                else:
                    url=request.session.get('url')
                    print('getting url',url)
                    print()
                    request.session['url']=None
                    
                    return HttpResponseRedirect(url)
            else:
                error_message='wrong password'
        
        return render(request,'store/login.htm',{'error':error_message})
    

def logout(request):
    request.session.clear()
    return redirect('login') 

def cart(request):
    ids=list(request.session.get('cart').keys())
    products=product.Product.get_by_id(ids)
    return render(request,'store/cart.htm',{'products':products})


def checkout(request):
    if not request.session.get('customer_id'):
        return_url='/cart'
        return redirect(f'login?return_url={return_url}')
    else:
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer_id=request.session.get('customer_id')
        cart=request.session.get('cart')
        products=product.Product.get_by_id(list(cart.keys()))
        print(cart)
        for p in products:
            print(customer_id)
            c=customer.Customer.get_by_id(customer_id)
            ob=orders.Orders(product=p,customer=c[0],quantity=cart[str(p.id)],price=p.price,phone=phone,address=address)
            ob.place_order()
        request.session['cart']={}

        return redirect('homepage')
@auth_middleware
def order_history(request):
    cus=request.session.get('customer_id')
    ords=orders.Orders.get_order_by_customer(cus)
    return render(request,'store/orders.htm',{'orders':ords})