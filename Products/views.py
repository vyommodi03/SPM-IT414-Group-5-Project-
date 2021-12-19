from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product
from django.views.generic.list import ListView
from django.views.generic import DetailView
from Cart.models import Order
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
# SellProducts Cloths ListView
class SellClothsList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    paginate_by = 10
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        object_list = Product.objects.filter(product_for='sell').filter(type__iexact='cloths').order_by("-timestamp")
        filtered_objects = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_projects = []

        page = request.GET.get('page', 1)
        paginator = Paginator(object_list, 10)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        if filtered_objects.exists():
            user_order = filtered_objects[0]
            user_order_items = user_order.items.all()
            current_order_projects = [product.product for product in user_order_items]

        return render(request, self.template_name, {
            'object_list': object_list,
            'current_order_projects': current_order_projects
        })


# SellProducts Accessories ListView
class SellAccessoriesList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    paginate_by = 10
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        object_list = Product.objects.filter(product_for='sell').filter(type__iexact='accessories').order_by("-timestamp")
        filtered_objects = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_projects = []

        page = request.GET.get('page', 1)
        paginator = Paginator(object_list, 10)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        if filtered_objects.exists():
            user_order = filtered_objects[0]
            user_order_items = user_order.items.all()
            current_order_projects = [product.product for product in user_order_items]

        return render(request, self.template_name, {
            'object_list': object_list,
            'current_order_projects': current_order_projects
        })


# RentProducts Cloths ListView
class RentClothsList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    paginate_by = 10
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        object_list = Product.objects.filter(product_for='rent').filter(type__iexact='cloths').order_by("-timestamp")
        filtered_objects = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_projects = []

        page = request.GET.get('page', 1)
        paginator = Paginator(object_list, 10)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        if filtered_objects.exists():
            user_order = filtered_objects[0]
            user_order_items = user_order.items.all()
            current_order_projects = [product.product for product in user_order_items]

        return render(request, self.template_name, {
            'object_list': object_list,
            'current_order_projects': current_order_projects
        })


# RentProducts Cloths ListView
class RentAccessoriesList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    paginate_by = 10
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        object_list = Product.objects.filter(product_for='rent').filter(type__iexact='accessories').order_by("-timestamp")
        filtered_objects = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_projects = []

        page = request.GET.get('page', 1)
        paginator = Paginator(object_list, 10)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        if filtered_objects.exists():
            user_order = filtered_objects[0]
            user_order_items = user_order.items.all()
            current_order_projects = [product.product for product in user_order_items]

        return render(request, self.template_name, {
            'object_list': object_list,
            'current_order_projects': current_order_projects
        })


# All SellProducts
class SellList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    paginate_by = 10
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        object_list = Product.objects.filter(product_for='sell').order_by("-timestamp")
        filtered_objects = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_projects = []

        page = request.GET.get('page', 1)
        paginator = Paginator(object_list, 10)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        if filtered_objects.exists():
            user_order = filtered_objects[0]
            user_order_items = user_order.items.all()
            current_order_projects = [product.product for product in user_order_items]

        return render(request, self.template_name, {
            'object_list': object_list,
            'current_order_projects': current_order_projects
        })


# All RentProducts
class RentList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    paginate_by = 10
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        object_list = Product.objects.filter(product_for='rent').order_by("-timestamp")
        filtered_objects = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_projects = []

        page = request.GET.get('page', 1)
        paginator = Paginator(object_list, 10)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        if filtered_objects.exists():
            user_order = filtered_objects[0]
            user_order_items = user_order.items.all()
            current_order_projects = [product.product for product in user_order_items]

        return render(request, self.template_name, {
            'object_list': object_list,
            'current_order_projects': current_order_projects
        })


# All Cloths ListView
class ClothsList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    paginate_by = 10
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        object_list = Product.objects.filter(type__iexact='cloths').order_by("-timestamp")
        filtered_objects = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_projects = []

        page = request.GET.get('page', 1)
        paginator = Paginator(object_list, 10)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        if filtered_objects.exists():
            user_order = filtered_objects[0]
            user_order_items = user_order.items.all()
            current_order_projects = [product.product for product in user_order_items]

        return render(request, self.template_name, {
            'object_list': object_list,
            'current_order_projects': current_order_projects
        })


# All Accessories ListView

class AccessoriesList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    paginate_by = 10
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        object_list = Product.objects.filter(type__iexact='accessories').order_by("-timestamp")
        filtered_objects = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_projects = []

        page = request.GET.get('page', 1)
        paginator = Paginator(object_list, 10)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        if filtered_objects.exists():
            user_order = filtered_objects[0]
            user_order_items = user_order.items.all()
            current_order_projects = [product.product for product in user_order_items]

        return render(request, self.template_name, {
            'object_list': object_list,
            'current_order_projects': current_order_projects
        })


class DiamondList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    paginate_by = 10
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        object_list = Product.objects.filter(type__iexact='diamonds').order_by("-timestamp")
        filtered_objects = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_projects = []

        page = request.GET.get('page', 1)
        paginator = Paginator(object_list, 10)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        if filtered_objects.exists():
            user_order = filtered_objects[0]
            user_order_items = user_order.items.all()
            current_order_projects = [product.product for product in user_order_items]

        return render(request, self.template_name, {
            'object_list': object_list,
            'current_order_projects': current_order_projects
        })

# All Products ListView
class Products(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    paginate_by = 15
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        object_list = Product.objects.all().order_by("-timestamp")
        filtered_objects = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_projects = []

        page = request.GET.get('page', 1)
        paginator = Paginator(object_list, 10)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        if filtered_objects.exists():
            user_order = filtered_objects[0]
            user_order_items = user_order.items.all()
            current_order_projects = [product.product for product in user_order_items]

        return render(request, self.template_name, {
            'object_list': object_list,
            'current_order_projects': current_order_projects
        })


# My Products ListView
class MyProductsList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    paginate_by = 15
    template_name = 'list.html'

    def get_queryset(self):
        products_list = Product.objects.filter(user__user__username__iexact=self.request.user.username)
        return products_list


# Featured SellProducts ListView
class FeaturedList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    paginate_by = 15
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        object_list = Product.objects.filter(featured=True).order_by("-timestamp")
        filtered_objects = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_projects = []

        page = request.GET.get('page', 1)
        paginator = Paginator(object_list, 10)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        if filtered_objects.exists():
            user_order = filtered_objects[0]
            user_order_items = user_order.items.all()
            current_order_projects = [product.product for product in user_order_items]

        return render(request, self.template_name, {
            'object_list': object_list,
            'current_order_projects': current_order_projects
        })


class SearchList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    paginate_by = 15
    template_name = 'list.html'

    def get_queryset(self):
        q = self.request.GET.get("product", None)
        if q is not None:
            products_list = Product.objects.filter(
                Q(title__icontains=q) |
                Q(description__icontains=q) |
                Q(category__iexact=q)|
                Q(type__icontains=q)
            ).order_by("-timestamp")
            return products_list


class SearchList1(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    paginate_by = 15
    template_name = 'list.html'

    def get_queryset(self):
        q = self.request.GET.get("product", None)
        q1 = self.request.GET.get("category", None)
        if q and q1 is not None:
            products_list = Product.objects.filter(
                (Q(title__icontains=q) | Q(description__icontains=q)) &
                Q(category__iexact=q1)
            )
            return products_list


# Traditional Wear ListView
class Traditional(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    paginate_by = 15
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        object_list = Product.objects.filter(category__exact="traditional").order_by("-timestamp")
        filtered_objects = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_projects = []

        page = request.GET.get('page', 1)
        paginator = Paginator(object_list, 10)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        if filtered_objects.exists():
            user_order = filtered_objects[0]
            user_order_items = user_order.items.all()
            current_order_projects = [product.product for product in user_order_items]

        return render(request, self.template_name, {
            'object_list': object_list,
            'current_order_projects': current_order_projects
        })


# Formal Wear ListView
class Formal(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    paginate_by = 15
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        object_list = Product.objects.filter(category__exact="formal").order_by("-timestamp")
        filtered_objects = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_projects = []

        page = request.GET.get('page', 1)
        paginator = Paginator(object_list, 10)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        if filtered_objects.exists():
            user_order = filtered_objects[0]
            user_order_items = user_order.items.all()
            current_order_projects = [product.product for product in user_order_items]

        return render(request, self.template_name, {
            'object_list': object_list,
            'current_order_projects': current_order_projects
        })


# Casual Wear ListView
class Casual(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    paginate_by = 15
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        object_list = Product.objects.filter(category__exact="casual").order_by("-timestamp")
        filtered_objects = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_projects = []

        page = request.GET.get('page', 1)
        paginator = Paginator(object_list, 10)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        if filtered_objects.exists():
            user_order = filtered_objects[0]
            user_order_items = user_order.items.all()
            current_order_projects = [product.product for product in user_order_items]

        return render(request, self.template_name, {
            'object_list': object_list,
            'current_order_projects': current_order_projects
        })


# Ethnic Wear ListView
class Ethnic(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    paginate_by = 15
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        object_list = Product.objects.filter(category__exact="ethnic").order_by("-timestamp")
        filtered_objects = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_projects = []

        page = request.GET.get('page', 1)
        paginator = Paginator(object_list, 10)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        if filtered_objects.exists():
            user_order = filtered_objects[0]
            user_order_items = user_order.items.all()
            current_order_projects = [product.product for product in user_order_items]

        return render(request, self.template_name, {
            'object_list': object_list,
            'current_order_projects': current_order_projects
        })


# Sports Wear ListView
class Sports(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    paginate_by = 15
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        object_list = Product.objects.filter(category__exact="sports").order_by("-timestamp")
        filtered_objects = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_projects = []

        page = request.GET.get('page', 1)
        paginator = Paginator(object_list, 10)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        if filtered_objects.exists():
            user_order = filtered_objects[0]
            user_order_items = user_order.items.all()
            current_order_projects = [product.product for product in user_order_items]

        return render(request, self.template_name, {
            'object_list': object_list,
            'current_order_projects': current_order_projects
        })


# Western Wear ListView
class Western(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    paginate_by = 15
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        object_list = Product.objects.filter(category__exact="western").order_by("-timestamp")
        filtered_objects = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_projects = []

        page = request.GET.get('page', 1)
        paginator = Paginator(object_list, 10)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        if filtered_objects.exists():
            user_order = filtered_objects[0]
            user_order_items = user_order.items.all()
            current_order_projects = [product.product for product in user_order_items]

        return render(request, self.template_name, {
            'object_list': object_list,
            'current_order_projects': current_order_projects
        })


# T-shirts ListView
class Tshirt(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    paginate_by = 15
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        object_list = Product.objects.filter(category__exact="t-shirts").order_by("-timestamp")
        filtered_objects = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_projects = []

        page = request.GET.get('page', 1)
        paginator = Paginator(object_list, 10)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        if filtered_objects.exists():
            user_order = filtered_objects[0]
            user_order_items = user_order.items.all()
            current_order_projects = [product.product for product in user_order_items]

        return render(request, self.template_name, {
            'object_list': object_list,
            'current_order_projects': current_order_projects
        })


# Kids Wear ListView
class Kids(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    paginate_by = 15
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        object_list = Product.objects.filter(category__exact="kids").order_by("-timestamp")
        filtered_objects = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_projects = []

        page = request.GET.get('page', 1)
        paginator = Paginator(object_list, 10)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        if filtered_objects.exists():
            user_order = filtered_objects[0]
            user_order_items = user_order.items.all()
            current_order_projects = [product.product for product in user_order_items]

        return render(request, self.template_name, {
            'object_list': object_list,
            'current_order_projects': current_order_projects
        })


# Jumpsuits ListView
class Jumpsuits(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    paginate_by = 15
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        object_list = Product.objects.filter(category__exact="jumpsuits").order_by("-timestamp")
        filtered_objects = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_projects = []

        page = request.GET.get('page', 1)
        paginator = Paginator(object_list, 10)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        if filtered_objects.exists():
            user_order = filtered_objects[0]
            user_order_items = user_order.items.all()
            current_order_projects = [product.product for product in user_order_items]

        return render(request, self.template_name, {
            'object_list': object_list,
            'current_order_projects': current_order_projects
        })


# Denim ListView
class Denim(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    paginate_by = 15
    template_name = 'list.html'


    def get(self, request, *args, **kwargs):
        object_list = Product.objects.filter(category__exact="denim").order_by("-timestamp")
        filtered_objects = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_projects = []

        page = request.GET.get('page', 1)
        paginator = Paginator(object_list, 10)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        if filtered_objects.exists():
            user_order = filtered_objects[0]
            user_order_items = user_order.items.all()
            current_order_projects = [product.product for product in user_order_items]

        return render(request, self.template_name, {
            'object_list': object_list,
            'current_order_projects': current_order_projects
        })


# DetailView
class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "single.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        instance = get_object_or_404(Product, slug=slug, sold=False)
        return instance


# Products CreateView
@login_required
def create(request, template_name='post.html'):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        f = form.save(commit=False)
        f.user = request.user.profile
        f.save()
        return redirect('list')
    else:
        messages.error(request, 'Please Correct the error below.')
        form = ProductForm()
    return render(request, template_name, {'form': form})

# Products EditView
@login_required
def edit(request, pk):
    template = 'post.html'
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Edited!')
        return redirect('my_list')
    return render(request, template, {'form': form})


# Products DeleteView
@login_required
def delete(request, pk):
    template = 'sell_delete.html'
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('my_list')
    return render(request, template, {'object': product})
