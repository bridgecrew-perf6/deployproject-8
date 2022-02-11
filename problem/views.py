from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .serializers import ProblemSerializer, ReplySerializer
from .models import *
from account.permissions import IsActive
from .permissions import IsAuthorPermission

class PermissionMixin:
    def get_permissions(self):
        if self.action == "create":
            permissions = [IsActive]
        elif self.action in ["update", "partial_update", "destroy"]:
            permissions = [IsAuthorPermission]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]


class ProblemViewSet(PermissionMixin ,ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context() # получаем контекст
        context["action"] = self.action
        return context


class ReplyViewSet(PermissionMixin,ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

