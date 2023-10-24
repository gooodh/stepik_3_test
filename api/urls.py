from rest_framework import routers

from api.views import GoodViewSet


router = routers.DefaultRouter()
router.register('good', GoodViewSet)

urlpatterns = []

urlpatterns.extend(router.urls)
