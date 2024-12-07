#incluir el include
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import EspecialidadViewSet, PacienteViewSet, MedicoViewSet, MedicamentoViewSet, RecetaViewSet, FormaFarmListView

router = DefaultRouter()

router.register('Especialidad', EspecialidadViewSet)
router.register('FormaFarm', FormaFarmListView, basename='formafarm')  # basename explícito
router.register('Paciente', PacienteViewSet)
router.register('Medico', MedicoViewSet)
router.register('Medicamento', MedicamentoViewSet)
router.register('Receta', RecetaViewSet)

#comentariar el urlpatterns de rutas de modelvieset
#urlpatterns = router.urls 

#copiar todo este urlpatterns
urlpatterns = [
#    path('',views.index, name='index'),
path('',include(router.urls)),
path('medicamento/filtrar/forma/', views.medicamentos_unidades, name="medicamento-unidades"),
]