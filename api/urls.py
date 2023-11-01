# from rest_framework import routers

# from api.views import GoodViewSet, TokenViewSet


# router = routers.DefaultRouter()
# router.register('good', GoodViewSet)
# router.register('get_token', TokenViewSet, basename='get_token')

# urlpatterns = []

# urlpatterns.extend(router.urls)

from django.urls import path
from .views import  TokenViewSet


urlpatterns = [
    # path('<int:pk>/', GoodViewSet.as_view()),
    path('get_token/', TokenViewSet.as_view(), name='get_token'),
    path('get_token/<int:pk>/', TokenViewSet.as_view(), name='get_token'),
]
