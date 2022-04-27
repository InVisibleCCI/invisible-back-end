from django.urls import include, path
from rest_framework_nested import routers

from merchant.views.merchant_viewset import MerchantViewSet
from merchant.views.navigation_tracker import NavigationTrackerViewSet

router = routers.DefaultRouter()

router.register('navigation-trackers', NavigationTrackerViewSet)
router.register('merchants', MerchantViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
