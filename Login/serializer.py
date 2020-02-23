#Importando librerías de Django
from rest_framework import routers,serializers,viewsets

#Importando el modelo del componente Login (desde el archivo models.py)
from Login.models import Example2

class Example2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Example2
        fields = ('__all__')