from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from perfumes.models import products, productsize
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    size_id=request.POST.get("sizeidd")
    cart = Cart(request)  # create a new cart object passing it the request object 
    
    product = get_object_or_404(products, id=product_id) 
    size_ = get_object_or_404(productsize , id=size_id)
    print(product)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,size_=size_, quantity=cd['quantity'], update_quantity=cd['update'])
        
    return redirect('cart:cart_detail')


def cart_remove(request, size_id):
    cart = Cart(request)
    #product = get_object_or_404(products, id=product_id)
    size_ = get_object_or_404(productsize , id=size_id)
    cart.remove(size_)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})
