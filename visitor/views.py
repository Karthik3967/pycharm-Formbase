from urllib import request

from django.shortcuts import render, redirect, get_object_or_404
from .models import Visitor
from .forms import visitorForm
def visitor_from_view(request):
    if request.method == 'POST':
        form = visitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = visitorForm()
        return render(request, 'Welcome/form.html', {'form': form})
def visitors_list(request):
    visitors = Visitor.objects.all()
    return render(request,'Welcome/visitor_list_.html', {'visitors': visitors})
def visitor_edit_list(request,id):
    visitor = get_object_or_404(Visitor,id=id)
    if request.method == 'POST':
        form =visitorForm(request.POST,instance=visitor)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = visitorForm(instance=visitor)
        return render(request,'Welcome/form.html', {'form': form,'edit':True})
def visitor_delete_list(request,id):
    visitor = get_object_or_404(Visitor,id=id)
    if request.method == 'POST':
        visitor.delete()
        return redirect('list')
    return render(request,'Welcome/visitor_delete.html',{'form':visitorForm(instance=visitor)})

