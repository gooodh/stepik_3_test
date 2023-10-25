from rest_framework import routers

from api.views import GoodViewSet, UserViewSet


router = routers.DefaultRouter()
router.register('good', GoodViewSet)
router.register('auth', UserViewSet)

urlpatterns = []

urlpatterns.extend(router.urls)
