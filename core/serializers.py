from rest_framework.serializers import ModelSerializer

from core.models import Marca, Categoria

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'