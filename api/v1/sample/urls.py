from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.sample.views import SampleViewSet

router = DefaultRouter()
router.register("sample", SampleViewSet, basename="common")


urlpatterns = [
    path("", include(router.urls)),
]
