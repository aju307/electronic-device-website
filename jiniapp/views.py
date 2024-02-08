from django.shortcuts import render,redirect
from jiniapp.models import catogorydb,productdb,Contact
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import messages

# Create your views here.
def shop(req):
    return render(req,'shop.html')
def shop1(req):
    return render(req,'shop1.html')
def addcatogory(req):
    return render(req,'addcatogory.html')
def savedata(req):
    if req.method == "POST":
        n = req.POST.get('name')
        d = req.POST.get('description')
        i = req.FILES['image']
        obj = catogorydb(Catogory_name=n,Description=d,Image=i)
        obj.save()
        messages.success(req,"Category saved successfully...!")
        return redirect(addcatogory)
def displaycatogory(req):
     data= catogorydb.objects.all()
     return render(req,'displaycatogory.html',{'data':data})
def editecatogory(req,dataid):
    cat = catogorydb.objects.get(id=dataid)
    return render(req,'editecatogory.html', {'cat':cat})
def updatecatogery(req,dataid):
    if req.method=="POST":
        n=req.POST.get('name')
        d=req.POST.get('description')
        try:
            img=req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file= catogorydb.objects.get(id=dataid).image
        catogorydb.objects.filter(id=dataid).update(Catogory_name=n,Description=d,Image=file)
        messages.success(req, "Category updated successfully...!")
        return redirect(displaycatogory)
def deletecatogory(req,dataid):
    data = catogorydb.objects.filter(id=dataid)
    data.delete()
    messages.success(req, "Category Deleted successfully...!")
    return redirect(displaycatogory)
def addproduct(req):
    catogory=catogorydb.objects.all()
    return render(req,'addproduct.html',{'catogory':catogory})
def saveproductdata(req):
    if req.method == "POST":
        c = req.POST.get('cat')
        n = req.POST.get('name')
        d = req.POST.get('description')
        p = req.POST.get('price')
        i = req.FILES['image']
        obj1 = productdb(Product_name=n,Description=d,Price=p,Image=i,Catogory_name=c)
        obj1.save()
        messages.success(req, "Product saved successfully...!")
        return redirect(addproduct)
def displayproduct(req):
    product = productdb.objects.all()
    return render(req,'displayproduct.html',{'product':product})
def editpdt(request,dataid):
    category = catogorydb.objects.all()
    data = productdb.objects.get(id=dataid)
    return render(request,"editproduct.html",{'category':category,'data':data})

def updatepdt(request,dataid):
    if request.method == "POST":
        c = request.POST.get('cat')
        bn = request.POST.get('name')
        desc = request.POST.get('desc')
        price = request.POST.get('price')

        try:
            img = request.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).Image
        productdb.objects.filter(id=dataid).update(Product_name=bn,Description=desc,Price=price,Image=file,Catogory_name=c)
        messages.success(request, "Product updated successfully...!")
        return redirect(displayproduct)

def deletepdt(req,dataid):
    data = productdb.objects.filter(id=dataid)
    data.delete()
    messages.success(req, "Product Deleted successfully...!")
    return redirect(displayproduct)

def admin_login(request):
    return render(request,"admin_login.html")

def adminlogin(request):
    if request.method == "POST":
        un = request.POST.get('user_name')
        pwd = request.POST.get('pas')

        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un,password=pwd)
            if user is not None:
                login(request,user)
                request.session['username'] = un
                request.session['password'] = pwd
                messages.success(request, "Welcome")

                return redirect(shop)
            else:
                messages.error(request, "Invalid username or password")
                return redirect(admin_login)
        else:
            return redirect(admin_login)


def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login)
def viewcontact(req):
    data = Contact.objects.all()
    return render(req,"viewcontact.html",{ 'data':data})

