from django.shortcuts import render, redirect
from django.urls import reverse

def index(request):
    return redirect(reverse("listings:all"))
