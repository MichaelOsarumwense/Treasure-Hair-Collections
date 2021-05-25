from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from products.models import Product
from django.db.models import Q


def do_search(request):
    """
    View for search page. Search results will be displayed in Products page
    """
    queries = Q(name__icontains=request.GET['q']) | Q(
                description__icontains=request.GET['q'])
    products = Product.objects.filter(queries)
    paginator = Paginator(products, 4)  # Show 4 products per page

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "products/products.html", {"products": products})
