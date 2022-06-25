from app.controllers.forms import checkbox_input, radio_input, select_tag, upload_file
from app.controllers.todo import delete_todo, edit_todo, index
from django.urls import path

urlpatterns = [
    path("", index, name="home"),
    path("person/<int:person_id>/", delete_todo, name="delete-todo"),
    path("person/edit/<int:person_id>/", edit_todo, name="edit-todo"),
]

# forms urls
urlpatterns += [
    path("upload/", upload_file, name="upload_file"),
    path("select/tag/", select_tag, name="select_tag"),
    path("radio/input/", radio_input, name="radio_input"),
    path("checkbox/input/", checkbox_input, name="checkbox_input"),
]
