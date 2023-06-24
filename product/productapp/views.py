from django.shortcuts import render,HttpResponse,redirect
from productapp.models import data
import json
# Create your views here.
def add(request):
    if request.method=='GET':

        return render(request,'add.html')
    else:
        n=request.POST['name']
        q=request.POST['quantity']
        t=request.POST['type']
        b=request.POST['batch']
        e=request.POST['expire']
        m=data.objects.create(name=n,quantity=q,type=t,batch=b,expire=e)

        m.save()
        context = {}
        context['count']=data.objects.all()
        return redirect('/dashboard')


def dashboard(request):
    context={}
    context['count']=data.objects.all()
    return render(request,'dashboard.html',context)

def delete(request,rid):
    k=data.objects.get(id=rid)

    k.delete()
    return redirect('/add')
        
    
def edit(request,rid):
    if request.method == 'GET':
        k=data.objects.get(id=rid)
        
        context= {}
        context['data']= k
        return render(request,'edit.html', context)
        
    else:
        n=request.POST['name']
        q=request.POST['quantity']
        t=request.POST['type']
        b=request.POST['batch']
        e=request.POST['expire']
        j=data.objects.get(id=rid)
        j.name = n
        j.quantity = q
        j.type = t
        j.batch = b
        j.expire = e
        j.save()
        context={}
        context['data']=j
        return redirect('/dashboard')