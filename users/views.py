from django.shortcuts import render
from rest_framework.views import APIView , Response
from rest_framework.parsers import JSONParser
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import VendorSerializer
from .models import Vendor, Customer
from rest_framework import permissions, status

# class LoginView(TokenObtainPairView):
#     permissions_classes = []


class VendorRegisterView(APIView):
    permissions_classes = [permissions.AllowAny]
    # authentication_classes = []
    # parser_classes = JSONParser

    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            vendor = Vendor.objects.create(
                email=request.data['email'],
                is_Vendor=True,
                name=request.data['name'],
                second_name=request.data['second_name'],
                phone_number=request.data['phone_number'],
                description=request.data['description'],
            )
            vendor.set_password(request.data['password'])
            vendor.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

