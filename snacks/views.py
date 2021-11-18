from django.db import models
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Snacks
from django.urls import reverse_lazy
# Create your views here.
class SnackListView(ListView):
    model =Snacks
    template_name = "snacks/snack_list.html"

class SnackDetailView(DetailView):
    template_name = "snacks/snack_detail.html"
    model = Snacks
    

class SnackCreateView(CreateView):
    template_name = "snacks/snack_create.html"
    model = Snacks
    context_object_name = 'object_things'
    fields = ['title','description','purchaser']

class SnackUpdateView(UpdateView):
    template_name = "snacks/snack_update.html"
    model = Snacks
    fields = ['title','description','purchaser']

class SnackDeleteView(DeleteView):
    template_name = "snacks/snack_delete.html"
    model = Snacks
    success_url = reverse_lazy('snack-list')
