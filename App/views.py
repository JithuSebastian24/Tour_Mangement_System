from re import sub
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from flask import request
from App.models import booking, package,Msg
from django.core.mail import send_mail

# Create your views here.
def index(req):
    return render(req,'index.html')

def packadv(req,type):
    if type=='ADVENTURE':
        obj=package.objects.filter(pcat="ADVENTURE")
        return render(req,"package.html",{'obj':obj})

def packholy(req,type):
    if type=='HOLYDAY':
        obj=package.objects.filter(pcat="HOLYDAY")
        return render(req,'package.html',{'obj':obj})

def packdev(req,type):
    if type=='DEVOTIONAL':
        obj=package.objects.filter(pcat="DEVOTIONAL")
        return render(req,'package.html',{'obj':obj})
        
def packhoney(req,type):
    if type=='HONEYMOON':
        obj=package.objects.filter(pcat="HONEYMOON")
        return render(req,'package.html',{'obj':obj})

def bookpack(req,id):
    obj=package.objects.get(id=id)
    return render(req,"booking.html",{'obj':obj})

def confirm(request):
    if request.method=='GET':
        return render(request,'booking.html')
    else:
        bname=request.POST.get('name')
        bemail=request.POST.get('email')
        bnum=request.POST.get('number')
        bpeople=request.POST.get('people')
        bcat=request.POST.get('category')
        bpack=request.POST.get('package')
        bdays=request.POST.get('days')
        bprice=request.POST.get('total')
        print(bname,bemail,bnum,bcat,bpack,bdays,bpeople,bprice)
        a=float(bpeople)
        b=float(bprice)
        print(type(a))
        print(type(b))
        x=a*b
        book={'bname':bname,'bemail':bemail,'bnum':bnum,'bpeople':bpeople,'bcat':bcat,'bpack':bpack,'bdays':bdays,'total':x}
        return render(request,"confirmation.html",{'book':book})

def booksave(request):
    if request.method=='GET':
        return render(request,"confirmation.html")
    else:
        cname=request.POST.get('name')
        cemail=request.POST.get('email')
        cpnum=request.POST.get('num')
        cpeople=request.POST.get('people')
        ccat=request.POST.get('category')
        cpack=request.POST.get('package')
        cdays=request.POST.get('days')
        ctotal=request.POST.get('total')
        booking.objects.create(bname=cname,bemail=cemail,bphoneno=cpnum,bpersonsno=cpeople,bcat=ccat,bpackname=cpack,bdays=cdays,btotalprice=ctotal)
        sub="Your Tour Booking Payment link And Cofirmation Mail-Magic Moments "
        msg="Dear  "+cname.upper()+", tour package you selected is "+cpack.upper()+". Its a  "+ccat.upper()+" package and the days covered in this tour is "+cdays.upper()+" ,you booked this tour for "+cpeople.upper()+" peoples and the total amount of your tour is $"+ctotal.upper()+" your payment link is given below. https://www.jpayindia.com/magicmoments/pay675e3876w32/236762625/&2dadad"
        email=cemail
        send_mail(sub,msg,settings.EMAIL_HOST_USER,[email],fail_silently=False)
    return render(request,"emailsuceess.html")
def msg(request):
    if request.method=='GET':
        return render(request,"index.html")
    else:
        coname=request.POST.get('username')
        coemail=request.POST.get('useremail')
        comsg=request.POST.get('message')
        Msg.objects.create(uname=coname,uemail=coemail,umsg=comsg)
        sub="Thank You For Your Contact"
        msg="Dear "+coname.upper()+",We recived your message we will send the replay soon"
        email=coemail
        send_mail(sub,msg,settings.EMAIL_HOST_USER,[email],fail_silently=False)
    return render(request,"index.html")

def rate(request):
    return render(request,'rating.html')

    