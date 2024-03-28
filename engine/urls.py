from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns = [
    path('auxi/', include('auxi.urls')),
    path('accounts/', include('accounts.urls')),
    path('modelsx/', include('modelsx.urls')),
    path('admin/', admin.site.urls),
    path('blueprint/schema/', SpectacularAPIView.as_view(), name='blueprint.schema'),
    path('blueprint/docs/', SpectacularSwaggerView.as_view(url_name='blueprint.schema'), name='blueprint.docs'),
]
