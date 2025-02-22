from django.shortcuts import render,redirect,HttpResponse
from .forms import signupform,login_form,password_change,profileform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from enroll.models import product ,cart,customer,orderplace
from django.db.models import Q
from django.views import View


def home(request):
    topwear=product.objects.filter(category="TW")
    bottomwear=product.objects.filter(category="BW")
    laptop=product.objects.filter(category="L")
    mobile=product.objects.filter(category="M")
    other=product.objects.filter(category="Other")
    return render(request,"home.html",{"topwear":topwear, "bottomwear":bottomwear, "laptop":laptop, "mobile":mobile, "other":other})


def product_details(request,pk):
    obj=product.objects.get(pk=pk)
    return render(request,'product _details.html',{"obj":obj})

def addtocart(request):
    user = request.user 
    product_id=request.GET["obj_id"]
    p_id=product.objects.get(id=product_id)
    obj=cart(user=user, product=p_id)
    obj.save()
    return redirect("cart")
def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart_data=cart.objects.filter(user=user)
        amount=0.0
        shipping_amount=70.0
        total_amount=0.0
        cart_product = [p for p in cart.objects.all() if p.user==user]
        if cart_product:
            for p in cart_product:
                tmpamount=(p.quantity * p.product.discount_price)
                amount=amount+tmpamount
                totalamount=amount+shipping_amount
            return render(request,'addtocart.html',{"cart":cart_data,"totalamount":totalamount,"amount":amount})
    return render(request,"addtocartempty.html")
def search(request):
    query=request.GET["search"]
    print(query)
    data=product.objects.filter(Q(title__icontains=query) | Q(discriptions__icontains=query) | Q(brand__icontains=query) | Q(category__icontains=query))
    return render(request,"search.html",{"data":data})   
def checkout(request):
    user=request.user
    address=customer.objects.filter(user=user)
    cart_items=cart.objects.filter(user=user)
    amount=0.0
    shipping_amount=70.0
    total_amount=0.0
    cart_product = [p for p in cart.objects.all() if p.user==user]
    if cart_product:
        for p in cart_product:
            tmpamount=(p.quantity * p.product.discount_price)
            amount=amount+tmpamount
        total_amount=amount+shipping_amount
    return render(request,"checkout.html",{"address":address,"total_amount":total_amount,"cart_items":cart_items,"amount":amount})
def payment_done(request):
    user=request.user
    custid=request.GET.get("custid")
    customer_name=customer.objects.get(id=custid)
    cart_data=cart.objects.filter(user=user)
    for c in cart_data:
        orderplace(user=user, customer=customer_name, product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect("order")
def order(request):
    user=request.user
    obj=orderplace.objects.filter(user=user)
    return render(request, 'orders.html',{"order":obj})



def profile(request):
    form=profileform()
    return render(request, 'profile.html',{"active":'btn-primary',"form":form})

class profileviewclass(View):
    def get(self, request):
        form=profileform()
        return render(request, 'profile.html',{"active":'btn-primary',"form":form})

    def post(self, request):
        form =profileform(request.POST)
        if form.is_valid():
            usr=request.user
            name=form.cleaned_data["name"]
            phone=form.cleaned_data["phone"]
            email=form.cleaned_data["email"]
            city=form.cleaned_data["city"]
            state=form.cleaned_data["state"]
            pincode=form.cleaned_data["pincode"]
            obj=customer(user=usr, name=name, phone=phone, email=email,city=city,state=state,pincode=pincode)
            obj.save()
            messages.success(request,"your data is successfuly upload!!!!!")
            form=signupform()
        return render(request,"profile.html",{"form":form})
        





def address(request): 
    return render(request, 'address.html',{"active":'btn-primary'})





def log_in(request):
    if request.method == "POST":
        form=login_form(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                # messages.success(request,"login successfully!!!!!!!!!!!!!!!!!!!")
                return redirect("home")
            
            form=login_form()
        else:
            messages.success(request," wrong password!!!!!!!!!!!!!!!!!!!")
    else:          
        form=login_form()
    return render(request,"login.html",{"form":form})
def singuppage(request):
    if request.method == "POST":
        form=signupform(request.POST)
        if form.is_valid():
            form.save()
            # return redirect("login")
            messages.success(request,"registrations is successfully!!!!!!!!!!!!!!!")
            form=signupform()
        else:
            return HttpResponse("password dose't' match...")
    else:
        form=signupform()
    return render(request,"signup.html",{"form":form})
def log_out(request):
    logout(request)
    return redirect("login")

# def password_changeform(request): 
#    if request.method == "POST":
#       fm = password_change(user=request.user, data=request.POST)
#       if fm.is_valid():
#          fm.save()
#          messages.success(request,"Password successfully change!!")
#         #  return HttpResponse("Password successfully change!!!")
#       else:
#           messages.success(request, "password too be wrong!!!!!!!!!!!!")  
    
#    else:
#         fm=password_change(user=request.user)
#    return render(request,"password_change.html",{"form":fm})

def topwear(request):
    return render(request, "topwear.html")