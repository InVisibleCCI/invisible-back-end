from django.urls import include, path
from rest_framework_nested import routers

from event.views.event_viewset import EventViewSet

router = routers.DefaultRouter()


router.register('events', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
