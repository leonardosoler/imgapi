from imagem.viewsets import ImagemViewSet, AnaliseViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('imagem', ImagemViewSet)
router.register('analise', AnaliseViewSet)
