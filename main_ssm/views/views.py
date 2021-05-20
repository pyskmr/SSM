# django imports
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password, check_password

# rest_framework imports
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token

# additional imports
from main_ssm.models.user_and_profile import User
from ..serializers import (
    UserLoginSerializer,
)
from ..permissions import checkCustomPermission, LoginCheckPermission
from ..components import CustomResponse


class Test(APIView):
    permission_classes = [checkCustomPermission]
    # authentication_classes = [LoginCheckPermission]

    def get(self, request):
        # print(dir(request))
        print(request.query_params)
        print(type(request.query_params))
        print(request.query_params["first_key"])
        res = {"Piyush": "ok this test is working fine"}
        return Response(res, status=status.HTTP_200_OK)


class LoginUser(APIView):
    def get(self, request):
        resp = CustomResponse()
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # If a user is authenticated then logout that user
        if request.user.is_authenticated:
            resp.add_additional_info_field(logged_out_user=str(request.user))
            logout(request)

        phone_number = serializer.validated_data.get("phone_number", "")
        password = serializer.validated_data.get("password", "")

        user_qs = User.objects.filter(phone_number=phone_number)

        if user_qs.exists():
            user = user_qs.first()
            if check_password(password, user.password):
                login(request, user)
                user_token = Token.objects.get(user=user).key
                resp.add_data_field(message="User successfully logged in")
                resp.add_data_field(token=user_token)
            else:
                resp.add_error_field(message="Please enter correct Password")
        else:
            resp.add_error_field(message="User doesn't exists")

        return Response(resp.get_response(), status=status.HTTP_200_OK)
