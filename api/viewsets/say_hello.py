from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
import datetime

class SayHelloViewSet(viewsets.ViewSet):
    
    @action(detail=False, methods=['get'])
    def hi(self, request):
        now = datetime.datetime.now()
        response_text = f"hola, son las {now.strftime('%-I:%M')}"
        return Response(response_text)
