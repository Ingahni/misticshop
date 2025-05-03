from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Category, Product
from cart.forms import CartAddProductForm

# для отображения глвавной страницы


def popular_list(request):
    # categories = Category.objects.all()
    products = Product.objects.filter(available=True)[:3]
    return render(request, 
                  'main/index/index.html',
                  {'products': products})
    
def product_detail(request, slug):
    product = get_object_or_404(Product, 
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm     # создаем кнопку добавления товара в корзину
    return render(request,
                  'main/product/detail.html',
                  {'product': product, 
                   'cart_product_form': cart_product_form})   
    # словарь с данными для шаблона
    # в качестве значения передаем объект product 
    # ключ product может называться как угодно
    # в шаблоне мы обращаемся к объекту product
    

# каталог товаров
def product_list(request, category_slug=None):
    page = request.GET.get('page', 1)
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    paginator = Paginator(products, 1)
    current_page = paginator.page(int(page))
    
    
    if category_slug:
        category = get_object_or_404(Category, 
                                     slug=category_slug)
        paginator = Paginator(products.filter(category=category), 1)
        current_page = paginator.page(int(page))
        # products = products.filter(category=category)
        
    return render(request,
                  'main/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': current_page,
                   'slug': category_slug})

