from django.shortcuts import render, get_object_or_404,redirect
from .models import Category, Product
from cart.forms import CartAddProductForm
from .forms import ContactForm


def product_detail(request, id, slug):
    print(id)
    categories = Category.objects.all()
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


def product_list(request, category_slug=None):
    category = None

    categories = Category.objects.all()
    products = Product.objects.filter(available=True, category_id=1)
    products2 = Product.objects.filter(available=True, category_id=2)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'products2': products2})


def contact(request):
    template_name = 'shop/product/contact.html'
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContactForm()
        context['form'] = form
    return render(request, template_name, context)
# Create your views here.

def category(request, pk):
    products = Product.objects.filter(category=pk)
    category = Category.objects.get(id=pk)
    categories = Category.objects.all()
    return render(request, 'shop/product/list.html', {'products': products, 'category': category, 'categories': categories})
