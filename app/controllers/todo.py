from django.shortcuts import redirect, render
from app.models import Person


def index(request, msg=''):
    # form submit 
    if request.method == "POST":
        person = Person()
        person.name = request.POST.get("name")
        if request.POST.get("age"):
            person.age = request.POST.get("age")
        person.address = request.POST.get("address")
        person.email = request.POST.get("email")
        person.save()
        msg = "Successfully added!"
    
    # show table data
    person_data = Person.objects.all()
    return render(request, "pages/index.html", {"data": person_data, "msg": msg})


def delete_todo(request, person_id):
    obj = Person.objects.get(id=person_id)
    obj.delete()
    return redirect("home")
