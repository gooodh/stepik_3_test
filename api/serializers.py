# from django.contrib.auth.models import User
from rest_framework import serializers

from django.contrib.auth.models import User

from api.models import Good


class GoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Good
        fields = ['name', 'amount', 'price']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', 'password']
        extra_kwargs = {'password': {'write_only': True}}
