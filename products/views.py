from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q, F
from django.db.models.functions import Lower
from .models import Product, Category, ProductVariant

def all_products(request):
    """A view to show all products, including sorting and search queries"""
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products:all_products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(ingredients__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}' if sort and direction else None

    featured_products = Product.objects.filter(is_featured=True)[:4]

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'featured_products': featured_products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to show individual product details"""
    product = get_object_or_404(Product, pk=product_id)
    variants = ProductVariant.objects.filter(product=product)
    
    context = {
        'product': product,
        'variants': variants,
    }

    return render(request, 'products/product_detail.html', context)


def product_category(request, category_name):
    """A view to show products filtered by category"""
    category = get_object_or_404(Category, name=category_name)
    products = Product.objects.filter(category=category)
    
    context = {
        'category': category,
        'products': products,
    }
    
    return render(request, 'products/products.html', context)


def skincare(request):
    """A view to show all skincare products"""
    skincare_categories = [
        'face_cleansers', 'serums', 'moisturizers', 
        'masks', 'eye_care', 'lip_care'
    ]
    
    products = Product.objects.filter(category__name__in=skincare_categories)
    categories = Category.objects.filter(name__in=skincare_categories)
    
    context = {
        'products': products,
        'current_categories': categories,
        'section_title': 'Skincare',
        'section_description': 'Discover our collection of premium skincare products designed to nourish, protect and enhance your skin.'
    }
    
    return render(request, 'products/category_landing.html', context)


def makeup(request):
    """A view to show all makeup products"""
    makeup_categories = ['face', 'eyes', 'lips', 'cheeks', 'brushes']
    
    products = Product.objects.filter(category__name__in=makeup_categories)
    categories = Category.objects.filter(name__in=makeup_categories)
    
    context = {
        'products': products,
        'current_categories': categories,
        'section_title': 'Makeup',
        'section_description': 'Express yourself with our range of high-quality makeup products for every look and occasion.'
    }
    
    return render(request, 'products/category_landing.html', context)


def body_hair(request):
    """A view to show all body and hair products"""
    body_hair_categories = ['bath', 'body_moisturizers', 'hair', 'fragrance']
    
    products = Product.objects.filter(category__name__in=body_hair_categories)
    categories = Category.objects.filter(name__in=body_hair_categories)
    
    context = {
        'products': products,
        'current_categories': categories,
        'section_title': 'Body & Hair',
        'section_description': 'Pamper yourself with luxurious body and hair products that cleanse, hydrate and delight your senses.'
    }
    
    return render(request, 'products/category_landing.html', context)


def special_offers(request):
    """A view to show all special offers"""
    featured_products = Product.objects.filter(is_featured=True)
    
    context = {
        'products': featured_products,
        'section_title': 'Special Offers',
        'section_description': 'Discover our featured products at incredible prices.'
    }
    
    return render(request, 'products/category_landing.html', context)
