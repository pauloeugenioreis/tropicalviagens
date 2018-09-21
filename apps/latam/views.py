from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.db.models import Count
import json
from django.http import HttpResponse
from apps.latam.models import Computer, Cadastros
from apps.latam.serializers import ComputerSerializer, CadastrosSerializer


@api_view(['GET'])
def pagamento(request):
    nome = request.GET.get('nome')
    versao = request.GET.get('versao')
    programa = request.GET.get('programa')
    model = {}
    if versao == 'v1':
        model = {'pagamento': True, 'cadastros': True, 'qtdCadastros': 20}
    else:
        model = {'pagamento': False, 'cadastros': True, 'qtdCadastros': 20}

    if(nome != None):
        computador = Computer(
            name=nome,
            programa=programa
        )
        computador.save()

    return JsonResponse(model)

@api_view(['GET'])
def total(request):
    Computer.objects.filter(name='DOM\\paulo.reis').delete()
    Computer.objects.filter(name='DELL-PAULO\\Paulo Eugenio').delete()
    queryset = Computer.objects.all().values('name').annotate(total=Count('name'))
    return JsonResponse({'Total': list(queryset)})

class ComputerViewSets(viewsets.ModelViewSet):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

class CadastrosViewSets(viewsets.ModelViewSet):
    queryset = Cadastros.objects.all()
    serializer_class = CadastrosSerializer