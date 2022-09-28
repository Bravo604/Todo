from rest_framework.viewsets import ModelViewSet
from .serializers import ToDoSerializer
from .models import Todo


class ToDoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer


# Create your views here.
