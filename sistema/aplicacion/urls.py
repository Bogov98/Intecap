from django.urls import path
from rest_framework import routers
from .api import projectViewSet

router = routers.DefaultRouter()
router.register('api/aplicacion', projectViewSet, 'aplicacion')

urlpatterns = router.urls
