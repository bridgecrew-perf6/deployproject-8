from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken, BlacklistedToken
from .serializers import *
from .models import User
from .permissions import *


class RegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response("Регистрация прошла успешно", status=status.HTTP_201_CREATED)


class ActivationView(APIView):
    def get(self, request, email, code):
        user = User.objects.get(email=email, activation_code=code)
        msg = (
            "Пользователь не найден",
            "Аккаунт активирован"
        )
        if not user:
            return Response(msg[0], status=status.HTTP_400_BAD_REQUEST)
        user.is_active = True
        user.activation_code = ""
        user.save()
        return Response(msg[-1], status=status.HTTP_200_OK)


    # permission_classes = (IsActive,)
class LogoutView(APIView):

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(token=refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
