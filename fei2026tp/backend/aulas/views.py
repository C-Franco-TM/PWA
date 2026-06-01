from django.shortcuts import render

# Create your views here.

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin

from .models import Carrera
from .serializers import CarreraSerializer


class CarreraMixin(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
