"""
URL configuration for pat_cad project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from pat_cadbackend import views  # Import views from your app

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'current_calls', views.CurrentCallViewSet, basename='currentcall')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # This will include all API endpoints managed by the router
    path('search-civilian/', views.search_civilian, name='search_civilian'),
    path('delete-call/<int:call_id>/', views.delete_call, name='delete_call'),
    path('create-call/', views.create_call, name='create_call'),
    path('api/register/', views.register, name='register'),  # Corrected import here
    path('api/login/', views.login, name='login'),  # Corrected import here
]
