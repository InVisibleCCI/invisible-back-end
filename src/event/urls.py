from django.urls import include, path
from rest_framework_nested import routers

from event.views.event_viewset import EventViewSet
from event.views.review_viewset import ReviewViewSet

router = routers.DefaultRouter()


router.register('events', EventViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
