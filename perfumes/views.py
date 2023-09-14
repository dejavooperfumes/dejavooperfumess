from django.shortcuts import render, redirect
from perfumes.models import *
from perfumes.forms import *
from django.db.models import Q
from django.contrib.auth import login, authenticate
from cart.forms import CartAddProductForm
from django.contrib import messages
import random

# Create your views here.
def home(request):
    e=products.objects.filter(tag='Top')
    l=products.objects.filter(tag='Luxury')[:3]
    return render(request,"home.html",{'e':e,'l':l})
def sbc(request):
    return render(request,"sbc.html")
def ori(request):
    d=products.objects.filter(type='Oriental')
    return render(request,"ori.html", {'d':d})
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def luxury(request):
    l=products.objects.filter(tag='Luxury')
    return render(request,"luxury.html",{'l':l})
def men(request):
    e=products.objects.filter(categoryid_id=1)
    return render(request,"men.html", {'e':e})
def women(request):
    e=products.objects.filter(categoryid_id=2)
    return render(request,"women.html", {'e':e})
def unisex(request):
    e=products.objects.filter(categoryid_id=3).filter(type='Perfume') 
    return render(request,"unisex.html", {'e':e})
def sbb(request):
    b=brand.objects.all()
    return render(request,"sbb.html",{'b':b})
def ARMANI(request):
    return render(request,"ARMANI.html")
def BURBERRY(request):
    return render(request,"BURBERRY.html")
def BVLGARI(request):
    return render(request,"BVLGARI.html")
def ck(request):
    return render(request,"ck.html")
def CAROLINA(request):
    return render(request,"CAROLINA.html")
def CHANEL(request):
    return render(request,"CHANEL.html")
def CREED(request):
    return render(request,"CREED.html")
def dior(request):
    return render(request,"dior.html")
def DG(request):
    return render(request,"DG.html")
def GIVENCHY(request):
    return render(request,"GIVENCHY.html")
def viewproduct(request,id):
    p=products.objects.filter(brandid_id=id)
    return render(request,"gucci.html",{'p':p})
def issey(request):
    return render(request,"issey.html")
def jaguar(request):
    return render(request,"jaguar.html")
def maison(request):
    return render(request,"maison.html")
def mont(request):
    return render(request,"mont.html")
def paco(request):
    return render(request,"paco.html")
def roja(request):
    return render(request,"roja.html")
def tomford(request):
    return render(request,"tomford.html")
def versace(request):
    return render(request,"versace.html")
def victoria(request):
    return render(request,"victoria.html")
def yves(request):
    return render(request,"yves.html")
def zara(request):
    return render(request,"zara.html")
def david(request):
    return render(request,"david.html")
def boss(request):
    return render(request,"boss.html")
def guess(request):
    return render(request,"guess.html")
def lacoste(request):
    return render(request,"lacoste.html")
def tommy(request):
    return render(request,"tommy.html")
def ferrari(request):
    return render(request,"ferrari.html")
def prada(request):
    return render(request,"prada.html")
def drakkar(request):
    return render(request,"drakkar.html")
def terre(request):
    return render(request,"terre.html")
def thank(request):
    return render(request,"thank.html")
def productdetail(request,id,bid):
    p=products.objects.get(id=id)
    ps=productsize.objects.filter(productid_id=id)
    r=review.objects.filter(productsid_id=id)
    proRANDOM = list(products.objects.all())
    morep=random.sample(proRANDOM ,15)
    cart_product_form = CartAddProductForm()
    return render(request,"PRODUCT.HTML",{'p':p,'r':r,'cart_product_form':cart_product_form,'morep':morep,'ps':ps})
def FAQ(request):
    return render(request,"FAQ.html")
def COU(request):
    return render(request,"COU.html")
def term(request):
    return render(request,"term.html")
def feedback(request):
    return render(request,"feedback.html")
def search(request):
    srh=request.GET['sname']
    p=products.objects.filter(name__icontains=srh)
    context={'p':p}
    return render(request,"gucci.html",context)
def insertcontact(request):
    if request.method=='POST':
        form=feedbackform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message is sent!')
            return redirect('/')
        
    else:
        form=feedbackform()
    return render(request,"feedback.html",{'form':form})



def sign(request):
    if request.method=='POST':
        form=SignForm(request.POST)
        if form.is_valid():
            try:
                user=form.save()
                login(request,user)
                return redirect('/')
            except:
                pass
    else:
        form=SignForm()
    return render(request,'registration/sign.html',{'form':form})

def insertreview(request):
    
    if request.method=='POST':
        form=reviewform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/thank')
    else:
        form=reviewform()
    return render(request,"product.html",{'form':form})
    