from django.shortcuts import render,redirect
from .forms import studentForm
from .models import student

# Create your views here.


def home(request):
    return render(request,'home.html')

def Registration(request):
    form = studentForm()
    if request.method =='POST':
        form = studentForm(request.POST)
        form.save()

    data = student.objects.all()
    return render(request,'Registration.html',{'form':form,'data':data})

def update(request,id):
    if request.method=='POST':
        data = student.objects.get(id=id)
        form = studentForm(request.POST,instance=data)
        form.save()
        return redirect('/Registration')
    else:
        data = student.objects.get(id=id)
        form = studentForm(instance=data)

    return render(request,'update.html',{'form':form})

def deletepage(request,id):

    a = student.objects.get(id=id)
    a.delete()
    return redirect('/Registration')