"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vehicle_garage.urls')), # URL to the vehicle garage
    path('auth/', include('rest_framework.urls')), # endpoint that prevents non-authenticated users from accessing dataset

    # Endpoints for Simple JWT
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'), # endpoint to get the first token
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'), # endpoint to allow token to be refreshed
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify') # endpoint for token verification
]
