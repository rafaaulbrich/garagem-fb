from django.contrib import admin

from .models import Marca, Categoria, Acessorio, Cor, Veiculo
from .serializers import MarcaSerializer, CategoriaSerializer, CorSerializer, AcessorioSerializer

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Acessorio)
admin.site.register(Cor)
admin.site.register(Veiculo)