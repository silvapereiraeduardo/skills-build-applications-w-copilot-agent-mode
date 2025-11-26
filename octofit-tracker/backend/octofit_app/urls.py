from rest_framework import routers
from .views import UserProfileViewSet, ActivityViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'activities', ActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
