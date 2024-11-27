from django.urls import path
from rental import views

urlpatterns = [
    path('offers/', views.OfferList.as_view()),
    path('offers/<int:pk>/', views.OfferDetails.as_view()),
]