from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import MarcaViewSet, CategoriaViewSet, AcessorioViewSet, CorViewSet, VeiculoViewSet

router = DefaultRouter()
router.register(r"marcas", MarcaViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"acessorios", AcessorioViewSet)
router.register(r"cores", CorViewSet)
router.register(r"veiculos", VeiculoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
]
