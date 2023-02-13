from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product_list.html'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    template_name = 'product_form.html'

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    template_name = 'product_form.html'

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')
    template_name = 'product_confirm_delete.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('product_list')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')