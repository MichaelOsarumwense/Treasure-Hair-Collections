from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.models import User
from products.models import Product
from django.http import HttpResponseRedirect
from .models import Favourites
from django.contrib.auth.decorators import login_required

"""
If the Product is already added to favourite then remove it from favourites.
If the Product is not in favourite then save it as favourite
"""
"""
@login_required so only authenticated users can have favourites list of products
"""


@login_required
def view_fav(request):

    favourite_products = Product.objects.filter(favourite=request.user)

    return render(request, 'favourite.html',
                  {"favourite_products": favourite_products})


@login_required
def add_remove_favourites(request, id):

    product = get_object_or_404(Product, pk=id)

    if product.favourite.filter(id=request.user.id).exists():
        product.favourite.remove(request.user)
    else:
        product.favourite.add(request.user)
    product.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
