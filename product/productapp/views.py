from django.shortcuts import render,HttpResponse,redirect
from productapp.models import data
import json
# Create your views here.
def add(request):

    # return render(request,'one.html')
    if request.method=='GET':

        return render(request,'one.html')
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
        return render(request,'one.html',context)


def dashboard(request):
    context={}
    context['count']=data.objects.all()
    return render(request,'dashboard.html',context)

def delete(request):
    if request.method == 'POST':
        string_data =request.body.decode("utf-8")
        json_data = json.loads(string_data)
        k=data.objects.get(id=json_data.get('id'))

        k.delete()
        return redirect('dash')
        
    
def edit(request):
    if request.method == 'GET':
        kid=request.GET.get('id')
        k=data.objects.get(id=kid)
        
        context= {}
        context['data']= k
        
        return render(request, 'edit.html', context)
        
    else:
      
        eid=request.POST['id']
        n=request.POST['name']
        q=request.POST['quantity']
        t=request.POST['type']
        b=request.POST['batch']
        e=request.POST['expire']
        j=data.objects.get(id=eid)
        j.name = n
        j.quantity = q
        j.type = t
        j.batch = b
        j.expire = e
        j.save()
        context={}
        context['data']=j
        return redirect('dash')