# from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Good


class GoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Good
        fields = ['name', 'amount', 'price']
