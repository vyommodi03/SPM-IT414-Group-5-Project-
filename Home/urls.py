from django.urls import path, include
from .views import *
from Products.views import SearchList1


urlpatterns = [
    path('', home, name='home'),
    path('search/', SearchList1.as_view(), name='search1'),
    path('contact/', contact, name='contact'),
    path('accounts/', include('allauth.urls')),
    path('products/', include('Products.urls')),
    path('profile/', profile, name='profile'),
    path('profile/edit/', editProfile, name='profile_edit'),
    path('profile/delete/<pk>/', deleteProfile, name='profile_delete'),
    path('help/', help, name='help'),
    path('feedback/', feedback, name='feedback'),
    path('cart/', include('Cart.urls', namespace='cart')),
    # path('cart1/', include('Cart1.urls', namespace='cart1')),
    path('howitworks/', howitworks, name='howitworks'),
    path('aboutus/', aboutus, name='aboutus'),
    path('faq/', faq, name='faq'),
    path('location/', location, name='location'),
]