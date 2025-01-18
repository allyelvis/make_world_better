from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Initiative
from .serializers import InitiativeSerializer

class InitiativeListView(APIView):
    def get(self, request):
        initiatives = Initiative.objects.all()
        serializer = InitiativeSerializer(initiatives, many=True)
        return Response(serializer.data)
