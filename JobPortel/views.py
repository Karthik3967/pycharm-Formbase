from urllib import request

from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import Employeeform

from . import views


def Employee_from_view(request):
    if request.method == 'POST':
        form = Employeeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = Employeeform()
        return render(request, 'Welcome/Form.html', {'form': form})
def  Employees_list(request):
    Employees = Employee.objects.all()
    return render(request,'Welcome/Employee_list_.html', {'Employees': Employees})
def Employee_change_list(request,id):
    Employee = get_object_or_404(Employees_list(),id=id)
    if request.method == 'POST':
        form =Employeeform(request.POST,instance=Employee)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = Employeeform(instance=Employee)
        return render(request,'Welcome/Form.html', {'form': form,'change':True})
def Employee_delete_list(request,id):
    Employee = get_object_or_404(Employees_list(),id=id)
    if request.method == 'POST':
        Employee.delete()
        return redirect('list')
    return render(request,'Welcome/Employee_delete.html',{'form':Employeeform(instance=Employee)})

