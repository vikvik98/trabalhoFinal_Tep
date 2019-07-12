from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework_jwt import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from filmes.models import *
from filmes.serializers import *


# Create your views here.

class FilmeList(generics.ListCreateAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    name = 'filme-list'
    authentication_classes = (JSONWebTokenAuthentication,)



class FilmeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    name = 'filme-datail'
    authentication_classes = (JSONWebTokenAuthentication,)



class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = 'categoria-list'
    authentication_classes = (JSONWebTokenAuthentication,)



class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = 'categoria-datail'
    authentication_classes = (JSONWebTokenAuthentication,)



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'Filmes': reverse(FilmeList.name, request=request),
            'categoria': reverse(CategoriaList.name, request=request),
            'usuarios': reverse(UserList.name, request=request)
        })

