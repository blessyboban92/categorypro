from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import auth, messages

from .models import *
app_name='finalapp'

def addcategory(request):
    categories = list(CategoryMaster.objects.all())
    categories.reverse()
    context = {
        'categories': categories
    }
    return render(request,'category.html',context)
def add_category(request):
    categories = CategoryMaster.objects.all()
    if request.method == "POST":
        categoryname= request.POST['categoryname']
        categorydescription = request.POST['categorydescription']
        Categories = CategoryMaster(categoryname=categoryname, categorydescription=categorydescription)
        Categories.save()
        messages.info(request, "Category added Successfully")
        return redirect('finalapp:add_category')
    context = {
        'categories': categories
    }
    return render(request,'category.html',context)
def delete_category(request,categoryid):
    categories=CategoryMaster.objects.get(id=categoryid)
    categories.delete()
    messages.info(request,"Category Deleted Successfully")
    return redirect('finalapp:add_category')
def update_category(request,categoryid):
    categories = CategoryMaster.objects.get(id=categoryid)
    categories.categoryname= request.POST['categoryname']
    categories.categorydescription = request.POST['categorydescription']
    categories.save()
    messages.info(request,"Category updated successfully")
    return redirect('finalapp:add_category')
def edit_category(request,categoryid):
    sel_categories=CategoryMaster.objects.get(id=categoryid)
    categories=CategoryMaster.objects.all()
    context = {
        'sel_categories':sel_categories,
        'categories':categories
    }
    return render(request, 'category.html', context)
