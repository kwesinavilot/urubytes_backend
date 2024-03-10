from django.urls import path
from .views import registerUser
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register'),
# ]

urlpatterns = [
    path('register/', registerUser, name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]