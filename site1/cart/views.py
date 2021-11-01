from django.shortcuts import redirect, render, get_object_or_404

from .forms import CartAddProductForm
from django.views.decorators.http import require_POST
from main.models import Engine
from .cart import Cart

@require_POST
def add(request, product_id):
    cart = Cart(request)
    engine = get_object_or_404(Engine, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=engine,
                 quantity=cd['quantity'],
                 update_quantity=cd['update']
                 )
        return redirect('cart:cart_detail')



def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})