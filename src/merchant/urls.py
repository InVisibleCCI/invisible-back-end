from django.urls import include, path
from rest_framework_nested import routers

from merchant.views.navigation_tracker import NavigationTrackerViewSet

router = routers.DefaultRouter()

router.register('navigation-trackers', NavigationTrackerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
