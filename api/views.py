from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import VehicleSerializer
from vehicles.models import Vehicle

@api_view(['GET'])
def getVehicles(request):
    vehicles=Vehicle.objects.all()
    serializer=VehicleSerializer(vehicles,many=True)
    return Response(serializer.data)
