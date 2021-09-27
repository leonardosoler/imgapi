from django.contrib import admin
from django.urls import path, include
from imagem.models import Analise, Imagem
from django.views.decorators.csrf import csrf_exempt
from imagem.views import (AnaliseView, index, ImagemView,
                          StatusAnaliseView, ImagemAnaliseView, AnaliseImagemView)
from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('imagem/', csrf_exempt(ImagemView)),
    path('analise/', csrf_exempt(AnaliseView)),
    path('imagem-analise/', csrf_exempt(ImagemAnaliseView)),
    path('status-analise/', csrf_exempt(StatusAnaliseView)),
    path('analise-imagem/', csrf_exempt(AnaliseImagemView)),
    path('api/', include(router.urls)),
]
