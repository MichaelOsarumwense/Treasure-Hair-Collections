from django.urls import path
from . import views

urlpatterns = [
    path('favourites', views.view_fav, name='view_fav'),
    path('addremove/<item_id>/', views.add_remove_favourites,
         name='add_remove_favourites'),
]
