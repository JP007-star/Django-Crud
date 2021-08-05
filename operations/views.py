from django.http.response import HttpResponse
from operations.models import Employee
from django.shortcuts import redirect, render
from operations.forms import EmployeeForm

# Create your views here.
def index(request):
    obj=Employee.objects.all()
    return render(request, 'index.html',{'data':obj})


def create(request):
    if request.method =="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read')
    else:
        form = EmployeeForm
    context={
        'form':form
    }
    return render(request, 'create.html',context)


def update(request,id):
    obj=Employee.objects.get(id=id)
    if request.method =="POST":
        form=EmployeeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('read')
    else:
        form = EmployeeForm
    context={
        'form':form
    }
    return render(request, 'update.html',context)


def delete(request,id):
    obj=Employee.objects.get(id=id)
    obj.delete()
    return redirect('read')

