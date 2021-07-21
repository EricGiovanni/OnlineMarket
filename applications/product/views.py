from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import (
    ListView,
)

from applications.person.models import User
from applications.person.mixins import SellerMixin
from .models import Product
from .forms import ProductForm

# Create your views here.
class RegisterView(SellerMixin, FormView):
    template_name = 'product/register.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_app:product_register')

    def form_valid(self, form):
        Product.objects.create(
            name=form.cleaned_data['name'],
            description=form.cleaned_data['description'],
            owner=self.request.user
        )
        return super(RegisterView, self).form_valid(form)

class ProductsSellerView(SellerMixin, ListView):
    template_name = 'product/seller_list.html'
    context_object_name = 'seller_list'
    paginate_by = 15

    def get_queryset(self):
        list_products = Product.objects.filter(
            owner=self.request.user
        ).order_by('id')
        return list_products
