from django.urls import path

from api.v1.views import CustomerCreateView, QuoteCreateUpdateView, PolicyDetailView, CustomerPoliciesListView

# router = DefaultRouter()
# router.register(r'policies', PolicyViewSet, basename='policy')

urlpatterns = [
    path('create_customer', CustomerCreateView.as_view(), name="create_customer"),
    path('quote', QuoteCreateUpdateView.as_view(), name="quote"),
    path('policies/<int:pk>', PolicyDetailView.as_view(), name="policy_detail"),
    path('policies', CustomerPoliciesListView.as_view(), name="customer_policies"),
]