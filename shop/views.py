from django.shortcuts import render, get_object_or_404
# get_object_or_404 >> 페이지 없음(404)
from .models import Product
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect, JsonResponse
from django.utils import timezone
from django.urls import reverse_lazy
import datetime
# Create your views here.
class IndexView(generic.ListView):
    template_name = "shop/home.html"
    context_object_name = "product_list"

    def get_queryset(self):
        return Product.objects.all()

class ProductDetailView(generic.DetailView):
        model = Product
        template_name = "shop/product_detail.html"