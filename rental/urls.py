from django.urls import path
from rental import views

urlpatterns = [
    path('offers/', views.offer_list),
    path('offers/<int:pk>/', views.offer_detail),
]