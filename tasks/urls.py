from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="indexurl"),
    path("delete/<str:pk>",views.delete, name="deleteurl"),
    path("edit/<str:pk>",views.edit, name="editurl"),

]