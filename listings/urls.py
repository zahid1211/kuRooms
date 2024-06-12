from django.urls import path
from . import views

app_name = "listings"

urlpatterns = [
    path("index/", views.MainView.as_view(), name="all"),
    path("create/", views.PropertyCreate.as_view(), name="create"),
    path("update/<int:pk>/", views.PropertyUpdate.as_view(), name="update"),
    path("delete/<int:pk>/", views.PropertyDelete.as_view(), name="delete"),
]