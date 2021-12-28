from django.urls import path
from .import views

urlpatterns = [
    path('',views.detail_dropdown),
    path('export/',views.export),
    

]