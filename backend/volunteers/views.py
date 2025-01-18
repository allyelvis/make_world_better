from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Volunteer
from .serializers import VolunteerSerializer

class VolunteerListView(APIView):
    def get(self, request):
        volunteers = Volunteer.objects.all()
        serializer = VolunteerSerializer(volunteers, many=True)
        return Response(serializer.data)
