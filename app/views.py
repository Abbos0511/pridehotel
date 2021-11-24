from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework import generics, permissions
from knox.models import AuthToken
from .serializer import *
from knox.views import LoginView as KnoxLoginView
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def post(self, request, *args, **kwargs):
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoomsView(viewsets.ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer

class BookRoomView(viewsets.ModelViewSet):
    queryset = BookRoom.objects.all()
    serializer_class = BookRoomSerializer

    # def retrieve(self, request, *args, **kwargs):
    #     queryset = BookRoom.objects.filter(rooms=kwargs['pk'])
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # def post(self, request, format=None):
    #     serializer=BookRoomserializer( data=request.data)
    #     print(serializer)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def list(self, request, *args, **kwargs):
    #     serializer=self.get_serializer(self.queryset, many=True)
    #
    #     return Response(serializer.data)



class ContactView(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    def update(self, request, *args, **kwargs):
        contact=Contact.objects.all()
        serializer=ContactSerializer(contact, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer=RoomsSerializer( data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# login.register
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self,request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
        })
class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)



