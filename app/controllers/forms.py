from django.shortcuts import render


def upload_file(request):
    if request.method == 'POST':
        print("POST data: ", request.POST)
        print("File data: ", request.FILES)
    return render(request, "pages/upload.html")

def select_tag(request):
    if request.method == 'POST':
        print("POST data: ", request.POST)
    return render(request, "pages/select.html")

def radio_input(request):
    if request.method == 'POST':
        print("POST data: ", request.POST)
    return render(request, "pages/radio.html")

def checkbox_input(request):
    if request.method == 'POST':
        print("POST data: ", request.POST)
        print("mylist", request.POST.getlist("mylist")) # for access all checkbox.. we get list here
    return render(request, "pages/checkbox.html")
