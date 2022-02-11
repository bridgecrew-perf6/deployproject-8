from django.urls import path, include
from problem.views import ProblemViewSet, ReplyViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("problem", ProblemViewSet)
router.register("reply", ReplyViewSet)

urlpatterns = [
    path("", include(router.urls)),
]