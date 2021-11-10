from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse
from .models import Engine, Category
from cart.forms import CartAddProductForm




def index(request):
    engines = Engine.objects.all()
    return render(request, "main/index.html", {"engins": engines})

def about(request):
    return render(request, "main/about.html", {})

def product_list(request, category_slug=None):
    category = None
    categoryes = Category.objects.all()
    engines = Engine.objects.filter(availbale=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        engines = Engine.objects.filter(category=category)
    else:
        engines = engines[:12]
    return render(request, "main/index.html", {"engins": engines, "category": category})

def product_detail(request, id, slug):
    product = Engine.objects.filter(id = id,
                                    slug = slug,
                                    availbale = True
                                    )[0]
    cart_product_form = CartAddProductForm
    return render(request, 'main/product_detale.html', {'engine': product,
                                                 'cart_product_form': cart_product_form})



# """методы, модетей"""










