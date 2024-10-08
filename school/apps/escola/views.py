from .models import Estudante, Curso, Matricula
from .serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer
from rest_framework import viewsets, generics, filters
from rest_framework.permissions import DjangoModelPermissions
from .pagination import SmallPagination, LargerPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from .throttles import MatriculaAnonRateThrottle

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all().order_by('id')
    serializer_class = EstudanteSerializer
    pagination_class = LargerPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('nome','cpf',)
    ordering_fields = ('nome',)
    http_method_names = ['get','post']


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by('id')
    serializer_class = CursoSerializer
    pagination_class = SmallPagination

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all().order_by('id')
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle,MatriculaAnonRateThrottle]

class ListaMatriculasCurso(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by('id')
        return queryset
    
    serializer_class = ListaMatriculasCursoSerializer

class ListaMatriculasEstudante(generics.ListAPIView):

    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by('id')
        return queryset
    
    serializer_class = ListaMatriculasEstudanteSerializer