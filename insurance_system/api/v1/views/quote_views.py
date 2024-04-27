from rest_framework import generics
from rest_framework import permissions, parsers

from api.v1.models import Quote
from api.v1.serializers import QuoteSerializer

class QuoteCreateUpdateView(generics.CreateAPIView, generics.UpdateAPIView):
    parser_classes = [parsers.JSONParser]
    permission_classes = [permissions.AllowAny]
    allowed_methods = ["POST", "PATCH"]
    
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        # make sure to catch 404's below
        obj = queryset.get(pk=self.request.data['quote_id'])
        self.check_object_permissions(self.request, obj)
        return obj
