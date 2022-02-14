from django.contrib import admin
from django.urls import path, include
from problem.views import ProblemViewSet
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register("problem", ProblemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include("account.urls")),
    path("api/v1/", include("problem.urls")),
    path("api/v1/", include("comment.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


