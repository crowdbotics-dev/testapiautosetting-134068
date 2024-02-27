from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors134068ViewSet

router = DefaultRouter()
router.register(
    "testconnectors134068", Testconnectors134068ViewSet, basename="testconnectors134068"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
