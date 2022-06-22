from django.db import IntegrityError
from django.shortcuts import redirect, render
from app.form.person_form import PersonForm
from app.models import Person


def index(request, msg=''):
    # form submit 
    try:
        if request.method == "POST":
            person = Person()
            forms = PersonForm(request.POST)
            if forms.is_valid():
                person.name = request.POST.get("name")
                if request.POST.get("age"):
                    person.age = request.POST.get("age")
                person.address = request.POST.get("address")
                person.email = request.POST.get("email")
                person.save()
                msg = "Successfully added!"
            else:
                msg = "Invalid form! Please fill required fields"

        # show table data
        person_data = Person.objects.all()
        return render(request, "pages/index.html", {"data": person_data, "msg": msg})
    except IntegrityError as e:
        msg = e.args[0]
        person_data = Person.objects.all()
        return render(request, "pages/index.html", {"data": person_data, "msg": msg})


def delete_todo(request, person_id):
    obj = Person.objects.get(id=person_id)
    obj.delete()
    return redirect("home")

def edit_todo(request, person_id, msg=''):
    person = Person.objects.get(id=person_id)
    
    # when form submitted then only goes inside of if condition ->
    if request.method == "POST":
        forms = PersonForm(request.POST)
        if forms.is_valid():
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.address = request.POST.get("address")
            person.email = request.POST.get("email")
            person.save()
            return redirect("home")
        else:
            msg = "Invalid form! Please fill required fields"
        
    return render(request, "pages/edit.html", {"data": person, "msg": msg})
