from django.urls import path
from app.views import TodoViewSet

urlpatterns = [
    path(r'todo/', TodoViewSet.as_view({'get': 'list', 'post': 'create'})),
    path(r'todo/<int:pk>/', TodoViewSet.as_view({'get': 'retrieve', 'put': 'partial_update', 'delete': 'destroy'})),
]