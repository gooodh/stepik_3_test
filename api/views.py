from rest_framework import viewsets
from api.models import Good

from api.serializers import GoodSerializer

# Create your views here.


class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
