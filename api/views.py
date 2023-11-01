from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from api.models import Good
# from django.contrib.auth.models import User
from uuid import uuid4
from django.utils.crypto import get_random_string

from api.serializers import GoodSerializer

# Create your views here.


class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer


class TokenViewSet(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        token = uuid4()
        return Response({'token': token})
