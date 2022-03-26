from django.urls import include, path
from rest_framework_nested import routers

from core.views.user import UserViewSet

router = routers.DefaultRouter()


router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
