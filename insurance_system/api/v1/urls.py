from django.urls import path

from .views import CustomerCreateView, QuoteCreateUpdateView

urlpatterns = [
    path('create_customer', CustomerCreateView.as_view(), name="create_customer"),
    path('quote', QuoteCreateUpdateView.as_view(), name="quote"),
]