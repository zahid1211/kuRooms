from django.shortcuts import render
from django.urls import reverse_lazy

from django.http import HttpResponse
from .models import Property
from .owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

class MainView(OwnerListView):
    model = Property
    fields = ["title", "address", "contact_1", "contact_2"]

class PropertyCreate(OwnerCreateView):
    model = Property
    fields = ["title", "address", "contact_1", "contact_2"]
    success_url = reverse_lazy("listings:all")

class PropertyUpdate(OwnerUpdateView):
    model = Property
    fields = ["title", "address", "contact_1", "contact_2"]
    success_url = reverse_lazy("listings:all")

class PropertyDelete(OwnerDeleteView):
    model = Property
    success_url = reverse_lazy("listings:all")