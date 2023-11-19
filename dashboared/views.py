from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
#from .decorators import auth_users, allowed_users

# Create your views here.

@login_required()
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    orders_count = orders.count()
    product_count = products.count()
    werkers_count = User.objects.all().count()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboared-index')
    else:
        form = OrderForm()
    context = {
        'form': form,
        'orders': orders,
        'products': products,
        'product_count': product_count,
        'orders_count': orders_count,
        'werkers_count': werkers_count,
    }
    return render(request,'dashboared/index.html',context)




@login_required()
def staff(request):
    werkers = User.objects.all()
    werkers_count = werkers.count()
    orders_count = Order.objects.all().count()
    product_count = Product.objects.all().count()
    context={
        'werkers':werkers,
        #'form': form,
        'werkers_count':werkers_count,
        'orders_count':orders_count,
        'product_count':product_count,
    }
    return render(request,'dashboared/staff.html', context)


def staff_detail(request,pk):
    werkers = User.objects.get(id=pk)
    
   
    
    context={
       'werkers':werkers,
        #'form': form,
    }
    return render(request,'dashboared/staff_detail.html',context)


@login_required()
def product(request):
    items=Product.objects.all() # using URM
    product_count = items.count()
    #items=Product.objects.raw('SELECT * FROM dashboared_product')
    werkers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboared-product')
        
        
    else:
        form = ProductForm()
    context={
        'items':items,
        'form': form,
        'werkers_count':werkers_count,
        'orders_count':orders_count,
        'product_count':product_count,
    }
    return render(request,'dashboared/product.html',context)



def product_delete(request,pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboared-product')
    context = {
        'item': item
    }
    return render(request, 'dashboared/product_delete.html', context)


@login_required(login_url='user-login')
#@allowed_users(allowed_roles=['Admin'])
def product_update(request, pk):  #matched except the the line before it
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboared-product')
    else:
        form = ProductForm(instance=item)
    
    context={
        'form': form,
    }
                
    return render(request, 'dashboared/product_update.html', context)




@login_required(login_url='user-login')
def order(request):  #matched
    orders = Order.objects.all()
    orders_count = orders.count()
    werkers_count = User.objects.all().count()
    product_count = Product.objects.all().count()
    
    #customer = User.objects.filter(groups=2)
    #customer_count = customer.count()
    #product = Product.objects.all()
    #product_count = product.count()

    context = {
        'orders': orders,
        'werkers_count':werkers_count,
        'product_count': product_count,
        'orders_count': orders_count,
    }
    return render(request, 'dashboared/order.html', context)

