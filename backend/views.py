from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import *
from .serializers import TodoSerializer

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
	serializer_class = TodoSerializer
	queryset         = Todo.objects.all()

def index(request): 
	context = [e for e in Todo.objects.values()]
	return render(request, 'index.html', context={'tasks': context})