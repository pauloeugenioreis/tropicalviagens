from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your views here.

    #def pagamento(self):
        #return JsonResponse({'pagamento': True})
from apps.latam.models import Computer
from apps.latam.serializers import ComputerSerializer


@api_view(['GET'])
def pagamento(request):
    nome = request.GET.get('nome')
    if(nome != None):
        computador = Computer(
            name=nome
        )
        computador.save()
    return JsonResponse({'pagamento': True})

class ComputerViewSets(viewsets.ModelViewSet):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer
