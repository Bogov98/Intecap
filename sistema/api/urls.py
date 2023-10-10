
from django.urls import include, path
from drf_spectacular.views import spectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from drf_spectacular.views import SpectacularAPIView


from api.views import UserViewSet

route: ExstendedSimpleRouter = ExtendedDefaultRouter()

router = routers.DefaultRouter()
route.register(r'users', UserViewSet)

urlpatterns = [
    path('shcema/', spectacularAPIView.as_view(), name='schema'),
    path('schema/swagger/', SpectacularSwaggerView.as_view(url_name='api:schema'), name='swagger'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_refresh'),
    path('', include(router.urls)),

]