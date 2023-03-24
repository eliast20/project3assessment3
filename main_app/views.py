from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy

from .models import Item


class WishList(ListView):
    model = Item
    template_name = 'wish_list.html'
    context_object_name = 'items'


class ItemCreateView(CreateView):
    model = Item
    template_name = 'item_form.html'
    fields = ['name', 'description', 'price']
    success_url = reverse_lazy('wish_list')


class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'item_confirm_delete.html'
    success_url = reverse_lazy('wish_list')
