from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import connections
from django.db.utils import OperationalError
from rest_framework import status

class LivenessView(APIView):
    authentication_classes = []  # Avoid auth for health checks
    permission_classes = []

    def get(self, request):
        return Response({'status': 'ok'}, status=status.HTTP_200_OK)

class ReadinessView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        try:
            # readiness logic here - cache, queue, external api
            connections['default'].cursor()
            return Response({'status': 'ready'}, status=status.HTTP_200_OK)
        except OperationalError:
            return Response({'status': 'unavailable'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
