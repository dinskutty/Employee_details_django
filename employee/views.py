from django.shortcuts import render,redirect
from employee.forms import EmployForm
from employee.models import Employ

# Create your views here.
def eemp(request):
    if request.method=='POST':
        form=EmployForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form=EmployForm()
    return render(request,'index.html',{'form':form})

def show(request):
    employees=Employ.objects.all()
    return render(request,"show.html",{'employees':employees})

def edit(request,id):
    employee=Employ.objects.get(id=id)
    return render(request,'edit.html',{'employee':employee})

def update(request,id):
    employee=Employ.objects.get(id=id)
    form=EmployForm(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,'edit.html',{'employee':employee})

def delt(request,id):
    employee=Employ.objects.get(id=id)
    employee.delete()
    return redirect('/show')