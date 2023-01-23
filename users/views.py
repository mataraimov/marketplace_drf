from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.parsers import JSONParser
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import VendorSerializer, CustomerSerializer, MyTokenObtainPairSerializer
from .models import Vendor, Customer
from rest_framework import permissions, status
from .permissions import AnonPermissions


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


class CustomerRegisterView(APIView):
    permissions_classes = [permissions.AllowAny]

    # authentication_classes = []
    # parser_classes = JSONParser

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer = Customer.objects.create(
                email=request.data['email'],
                name=request.data['name'],
                second_name=request.data['second_name'],
                phone_number=request.data['phone_number'],
                description=request.data['description'],
                cart_number=request.data['cart_number'],
                address=request.data['address'],
                post_code=request.data['description'],
            )
            customer.set_password(request.data['password'])
            customer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class VendorListApiView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def get(self, request):
        snippets = Vendor.objects.all()
        serializer = VendorSerializer(snippets, many=True)
        return Response(serializer.data)


class CustomerListApiView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def get(self, request):
        snippets = Customer.objects.all()
        serializer = CustomerSerializer(snippets, many=True)
        return Response(serializer.data)


class VendorApiView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def get_object(self, id):
        try:
            return Vendor.objects.get(id=id)
        except:
            return Http404

    def get(self, request, id):
        snippet = self.get_object(id)
        serializer = VendorSerializer(snippet)
        return Response(serializer.data)


class CustomerApiView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def get_object(self, id):
        try:
            return Customer.objects.get(id=id)
        except:
            return Http404

    def get(self, request, id):
        snippet = self.get_object(id)
        serializer = CustomerSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, id):
        snippet = self.get_object(id)
        serializer = CustomerSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LoginView(TokenObtainPairView):
    permission_classes = (AnonPermissions,)
    serializer_class = MyTokenObtainPairSerializer
