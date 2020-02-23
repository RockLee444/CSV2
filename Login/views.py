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
from Login.models import Example2

#Importación de serializer
from Login.serializer import Example2Serializer

class CustomAuthToken(ObtainAuthToken):
    
    def post(self, request, * args, **kwars):
        serializer = self.serializer_class (data = request.data, 
                                            context = {
                                                    'request': request, 
                                                    }
                                            )
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'it_works': 'IT WORKED! Keep up the great work!',
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })

class Example2List(APIView):
    
    def get(self,request,format=None):
        print("Realizando consulta...")
        queryset = Example2.objects.filter(delete=False)
        #many = True #(Solo si se van a retornar múltiples objetos)
        serializer = Example2Serializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = Example2Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            newData = serializer.data
            return Response(newData)
        return Response(serializer.errors, status  = status.HTTP_400_BAD_REQUEST)
    