from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Especialidad, FormaFarm, Paciente, Medico, Medicamento, Receta
from .serializers import EspecialidadSerializer, FormaFarmSerializer, PacienteSerializer, MedicoSerializer, MedicamentoSerializer, RecetaSerializer
from rest_framework.decorators import api_view

# Create your views here.
#def index(request):
#    return HttpResponse("Esta es la página principal de la app saludapp.")
def index(request):
    return HttpResponse(request, "Esta es la página principal de la app saludapp.")

# ModelViewSet
class EspecialidadViewSet(ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class FormaFarmListView(ModelViewSet):
    def list(self, request):
        choices = [{"value": choice.value, "label": choice.label} for choice in FormaFarm]
        return Response(request, choices)

class PacienteViewSet(ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class MedicoViewSet(ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class MedicamentoViewSet(ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class RecetaViewSet(ModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer

#incluir para el apicustomizado
@api_view(['GET'])
def medicamentos_unidades(request):
    try:
        medicamentos = Medicamento.objects.filter(forma='com')
        return JsonResponse(MedicamentoSerializer(medicamentos, many=True).data, safe=False, status=200)
    except Exception as e:
        return JsonResponse({"error":str(e)}, safe=False, status=500)