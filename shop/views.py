from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product
from django.utils import timezone
import datetime

class IndexView(generic.ListView):
    model = Product
    template_name = "shop/index.html"
    context_object_name = "shop_list"

    
