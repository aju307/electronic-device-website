from django.shortcuts import render,redirect
from frontend.models import Registration,cartdb
from jiniapp.models import catogorydb,productdb,Contact
from django.contrib import messages


# Create your views here.
def home(req):
    d = catogorydb.objects.all()
    return render(req,'home.html',{'d':d})
def products(req):
    pdt = productdb.objects.all()
    return render(req,'products.html',{'pdt':pdt})
def single_product(req,pdtid):
    data = productdb.objects.get(id=pdtid)

    return render(req,'single_product.html',{'data':data})
def product_filters(req,catname):
    data = productdb.objects.filter(Catogory_name=catname)
    return render(req,'product_filters.html',{'data':data})
def about(req):
    return render(req,'about.html')
def services(req):
    return render(req,'services.html')
def contactus(req):
    return render(req,'contactus.html')
def contactdata(request):
    if request.method == "POST":
        name = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        sub = request.POST.get('sub')
        msg = request.POST.get('msg')
        obj = Contact(First_Name=name,Last_Name=lname,Email=email,Subject=sub,Message=msg)
        obj.save()
        return redirect(contactus)
def Reg(req):
    return render(req,'Reg.html')
def regdata(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mob = request.POST.get('mob')
        email = request.POST.get('email')
        user = request.POST.get('username')
        pas = request.POST.get('pas')
        obj = Registration(Name=name,Mobile=mob,Email=email,Username=user,Password=pas)
        obj.save()
        return redirect(Reg)
def loginpage(req):
    return render(req, "Reg.html")
def userlogin(request):
    if request.method == "POST":
        un = request.POST.get('loginus')
        pwd = request.POST.get("loginpwd")
        if Registration.objects.filter(Username=un, Password=pwd).exists():
            request.session['Username'] =un
            request.session['Password'] =pwd
            messages.success(request, "Welcome")
            return redirect(home)
        else:
            messages.error(request, "Invalid username or password")
            return redirect(Reg)

    return redirect(Reg)
def logout(request):
    del request.session['Username']
    del request.session['Password']
    messages.success(request, "Logouted successfully")
    return redirect(loginpage)
def cart(request):
    ca = cartdb.objects.filter(Username=request.session['Username'])
    total_price = 0
    for i in ca:
        total_price=total_price+i.Total_price

    return render(request,'cart.html',{'ca':ca,'total_price':total_price})
def savecart(request):
    if request.method == "POST":
        qu = request.POST.get('quantity')
        tp = request.POST.get('tprice')
        de = request.POST.get('description')
        pn = request.POST.get('pname')
        un = request.POST.get('username')
        obj = cartdb(Username =un,Quantity = qu,Total_price = tp,Description = de, Product_name = pn)
        obj.save()
        messages.success(request, "Successfully added item to the cart")
        return redirect(cart)
def deletecart(request,pro_id):
    pro = cartdb.objects.filter(id=pro_id)
    pro.delete()
    messages.success(request, "Successfully Deleted item from the cart")
    return redirect(cart)
def checkout(request):
    ca = cartdb.objects.filter(Username=request.session['Username'])
    total_price = 0
    for i in ca:
        total_price = total_price + i.Total_price
    return render(request,"checkout.html",{'ca':ca,'total_price':total_price})