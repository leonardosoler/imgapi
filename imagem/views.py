from django.http.response import HttpResponse
from django.http import JsonResponse
from .serializers import ImagemSerializer, AnaliseSerializer
from .models import (Imagem, Analise)
from rest_framework import status
from imagem.models import Imagem, Analise
from imagem.serializers import ImagemSerializer, AnaliseSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def ImagemView(request):

    if request.method == 'GET':
        imagem = Imagem.objects.all()

        try:
            id_imagem = request.data['id_imagem']
        except:
            id_imagem = None
        if id_imagem is not None:
            imagem = imagem.filter(id_imagem=id_imagem)

        imagens_serializer = ImagemSerializer(imagem, many=True)
        return JsonResponse(imagens_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':

        imagem = (request.data)
        imagem_serializer = ImagemSerializer(data=request.data)

        if imagem_serializer.is_valid():
            imagem_serializer.save()
            return JsonResponse(imagem_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(imagem_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            imagem = Imagem.objects.get(id_imagem=request.data['id_imagem'])
        except Imagem.DoesNotExist:
            return JsonResponse({'message': 'A imagem não existe!'}, status=status.HTTP_404_NOT_FOUND)

        id_imagem = (request.data)
        imagem_serializer = ImagemSerializer(
            imagem, data=id_imagem, partial=True)

        if imagem_serializer.is_valid():
            imagem_serializer.save()
            return JsonResponse(imagem_serializer.data)
        return JsonResponse(imagem_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':

        try:
            id_imagem = request.data['id_imagem']
            count = Imagem.objects.filter(id_imagem=id_imagem).delete()
            message_text = 'A imagem com o id ' + \
                str(id_imagem) + 'e todos as suas analises foram apagadas.'
        except:
            count = Imagem.objects.all().delete()
            message_text = 'Todas as suas imagens e analises foram apagadas'

    return JsonResponse({'message': message_text}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def AnaliseView(request):

    if request.method == 'GET':
        analise = Analise.objects.all()

        try:
            id_analise = request.data['id_analise']
        except:
            id_analise = None
        if id_analise is not None:
            analise = analise.filter(id_analise=id_analise)

        analise_serializer = AnaliseSerializer(analise, many=True)
        return JsonResponse(analise_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':

        analise = (request.data)
        analise_serializer = AnaliseSerializer(data=request.data)

        if analise_serializer.is_valid():
            analise_serializer.save()

            imagem = Analise.objects.filter(
                id_imagem=analise_serializer.data['id_imagem'])
            imagens_serializer = AnaliseSerializer(imagem, many=True)

            return JsonResponse(imagens_serializer.data, safe=False)
        return JsonResponse(analise_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            analise = Analise.objects.get(
                id_analise=request.data['id_analise'])
        except Analise.DoesNotExist:
            return JsonResponse({'message': 'A analise não existe!'}, status=status.HTTP_404_NOT_FOUND)

        id_analise = (request.data)
        analise_serializer = AnaliseSerializer(
            analise, data=id_analise, partial=True)

        if analise_serializer.is_valid():
            analise_serializer.save()
            return JsonResponse(analise_serializer.data)
        return JsonResponse(analise_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':

        try:
            id_analise = request.data['id_analise']
            count = Analise.objects.filter(id_analise=id_analise).delete()
            message_text = 'A analise com o id ' + \
                str(id_analise) + ' foi apagada!'
        except:
            count = Analise.objects.all().delete()
            message_text = 'Todas as suas imagens foram apagadas'

    return JsonResponse({'message': message_text}, status=status.HTTP_204_NO_CONTENT)


def index(request):
    return HttpResponse('Hello World!')


@api_view(['PUT'])
def StatusAnaliseView(request):
    id_analise = None
    id_imagem = None

    try:
        id_analise = request.data['id_analise']
    except:
        id_imagem = request.data['id_imagem']

    data = (request.data)
    if id_analise is not None:
        analise = Analise.objects.get(id_analise=id_analise)
        analise_serializer = AnaliseSerializer(
            analise, data=data, partial=True)
        if analise_serializer.is_valid():
            analise_serializer.save()
            return JsonResponse(analise_serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(analise_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        analise_imagem = Analise.objects.filter(
            id_imagem=id_imagem).update(status = request.data['status'])
        analise_list = Analise.objects.filter(id_imagem=id_imagem)
        analise_serializer = AnaliseSerializer(
            analise_list, data=data, partial=True, many=True)
        if analise_serializer.is_valid(): 
            return JsonResponse(analise_serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(analise_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def ImagemAnaliseView(request):

    analise = Analise.objects.all()
    imagem = Imagem.objects.all()
    try:
        id_imagem = request.data['id_imagem']
    except:
        id_imagem = None
    if id_imagem is not None:
        imagem = Analise.objects.filter(id_imagem=id_imagem)
        imagens_serializer = AnaliseSerializer(imagem, many=True)
        return JsonResponse(imagens_serializer.data, safe=False)
    else:
        return JsonResponse({'message': 'Favor inserir um id_imagem para fazer a pesquisa!'}, safe=False)

    # 'safe=False' for objects serialization


@api_view(['GET'])
def AnaliseImagemView(request):

    analise = Analise.objects.all().order_by('id_imagem')

    imagens_serializer = AnaliseSerializer(analise, many=True)
    return JsonResponse(imagens_serializer.data, safe=False)
    # 'safe=False' for objects serialization
