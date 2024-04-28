from django.urls import path

from api.v1.views import *



urlpatterns = [
    path('create_customer', CustomerCreateView.as_view(), name="create_customer"),

    path('quote', QuoteCreateUpdateView.as_view(), name="quote"),

    path('policies', CustomerPoliciesListView.as_view(), name="customer_policies"),
    path('policies/<int:pk>', PolicyDetailWOHistoryView.as_view(), name="policy_detail"),
    path('policies/<int:pk>/history', PolicyDetailView.as_view(), name="policy_history"),

    path('search', CustomerSearchAPIView.as_view(), name="search_customer"),
    # path('search/policies', CustomerSearchAPIView.as_view(), name="search_customer"),
]