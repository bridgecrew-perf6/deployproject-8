from django.contrib import admin
from django.urls import path, include
from problem.views import ProblemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("problem", ProblemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include("account.urls")),
    path("api/v1/", include("problem.urls")),
    path("api/v1/", include("comment.urls")),
]

