from app.controllers.todo import delete_todo, index
from django.urls import path

urlpatterns = [
    path("", index, name="home"),
    path("person/<int:person_id>/", delete_todo, name="delete-todo"),
]
