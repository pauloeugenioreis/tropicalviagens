from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your views here.

    #def pagamento(self):
        #return JsonResponse({'pagamento': True})

@api_view(['GET'])
def pagamento(request):
    return JsonResponse({'pagamento': True})

