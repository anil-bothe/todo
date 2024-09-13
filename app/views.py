from rest_framework import viewsets
from app.models import *
from app.serializer import *


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)