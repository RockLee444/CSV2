from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

#Importación de librerías para errores u obtener objetos
from django.shortcuts import get_object_or_404
from django.http import Http404

#Importación de librerías para API Rest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

#Importación de modelo
from Profile.models import ProfileModel, CiudadModel, GeneroModel, OcupacionModel,EstadoModel,EstadoCivilModel

#Importación de serializer
from Profile.serializer import ProfileSerializer, ProfileGetSerializer, CiudadSerializer
from Profile.serializer import GeneroSerializer, OcupacionSerializer, EstadoSerializer
from Profile.serializer import EstadoCivilSerializer 

class ProfileList(APIView):
    
    def get(self,request,format=None):
        print("Realizando consulta...")
        #people = Person.objects.all().only(fields)
        queryset = ProfileModel.objects.filter(delete=False)
        #many = True #(Solo si se van a retornar múltiples objetos)
        serializer = ProfileSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            newData = serializer.data
            return Response(newData)
        return Response(serializer.errors, status  = status.HTTP_400_BAD_REQUEST)

class CiudadList(APIView):
    
    def get(self,request,format=None):
        print("Realizando consulta...")
        #people = Person.objects.all().only(fields)
        queryset = CiudadModel.objects.filter(delete=False)
        #many = True #(Solo si se van a retornar múltiples objetos)
        serializer = CiudadSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = CiudadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            newData = serializer.data
            return Response(newData)
        return Response(serializer.errors, status  = status.HTTP_400_BAD_REQUEST)    

class GeneroList(APIView):
    
    def get(self,request,format=None):
        print("Realizando consulta...")
        #people = Person.objects.all().only(fields)
        queryset = GeneroModel.objects.filter(delete=False)
        #many = True #(Solo si se van a retornar múltiples objetos)
        serializer = GeneroSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = GeneroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            newData = serializer.data
            return Response(newData)
        return Response(serializer.errors, status  = status.HTTP_400_BAD_REQUEST)

class OcupacionList(APIView):
    
    def get(self,request,format=None):
        print("Realizando consulta...")
        #people = Person.objects.all().only(fields)
        queryset = OcupacionModel.objects.filter(delete=False)
        #many = True #(Solo si se van a retornar múltiples objetos)
        serializer = OcupacionSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = OcupacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            newData = serializer.data
            return Response(newData)
        return Response(serializer.errors, status  = status.HTTP_400_BAD_REQUEST)

class EstadoList(APIView):
    
    def get(self,request,format=None):
        print("Realizando consulta...")
        #people = Person.objects.all().only(fields)
        queryset = EstadoModel.objects.filter(delete=False)
        #many = True #(Solo si se van a retornar múltiples objetos)
        serializer = EstadoSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = EstadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            newData = serializer.data
            return Response(newData)
        return Response(serializer.errors, status  = status.HTTP_400_BAD_REQUEST)

class EstadoCivilList(APIView):
    
    def get(self,request,format=None):
        print("Realizando consulta...")
        #people = Person.objects.all().only(fields)
        queryset = EstadoCivilModel.objects.filter(delete=False)
        #many = True #(Solo si se van a retornar múltiples objetos)
        serializer = EstadoCivilSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = EstadoCivilSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            newData = serializer.data
            return Response(newData)
        return Response(serializer.errors, status  = status.HTTP_400_BAD_REQUEST)