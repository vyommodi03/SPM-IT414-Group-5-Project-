from django.urls import path, include
from .views import *


urlpatterns = [
    path('', Products.as_view(), name='list'),
    path('search/', SearchList.as_view(), name='search'),
    path('myproducts/', MyProductsList.as_view(), name='my_list'),
    path('sellproducts/cloths/', SellClothsList.as_view(), name='sell_cloths_list'),
    path('sellproducts/accessories/', SellAccessoriesList.as_view(), name='sell_accessories_list'),
    path('rentproducts/cloths/', RentClothsList.as_view(), name='rent_cloths_list'),
    path('rentproducts/accessories/', RentAccessoriesList.as_view(), name='rent_accessories_list'),
    path('sellproducts/', SellList.as_view(), name="sell_list"),
    path('rentproducts/', RentList.as_view(), name="rent_list"),
    path('cloths/', ClothsList.as_view(), name='cloths'),
    path('accessories/', AccessoriesList.as_view(), name="accessories"),
    path('featured/', FeaturedList.as_view(), name='featured'),
    path('traditional/', Traditional.as_view(), name='traditional'),
    path('formal/', Formal.as_view(), name='formal'),
    path('casual/', Casual.as_view(), name='casual'),
    path('ethnic/', Ethnic.as_view(), name='ethnic'),
    path('sports/', Sports.as_view(), name='sports'),
    path('western/', Western.as_view(), name='western'),
    path('tshirts/', Tshirt.as_view(), name='tshirts'),
    path('kids/', Kids.as_view(), name='kids'),
    path('jumpsuits/', Jumpsuits.as_view(), name='jumpsuits'),
    path('denim/', Denim.as_view(), name='denim'),
    path('new/', create, name='new'),
    path('edit/<pk>/', edit, name='edit'),
    path('delete/<pk>/', delete, name='delete'),
    path('sellproducts/<slug>/', DetailView.as_view(), name='detail'),
    path('diamond/',DiamondList.as_view(),name='diamond_list'),
]

