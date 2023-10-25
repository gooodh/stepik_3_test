from rest_framework import viewsets
from api.models import Good
from django.contrib.auth.models import User

from api.serializers import GoodSerializer, UserSerializer

# Create your views here.


class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
