from django.shortcuts import render
from .models import VerbalAutopsy

# Create your views here.

def home(request):
    return render(request, "va/home.html")

def record_list(request):
    records = VerbalAutopsy.objects.all()
    return render(request, "va/record_list.html", {"records": records})

def add_record(request):
    if request.method == "POST":
        form = VerbalAutopsyForm(request.POST)
        
    if form.is_valid():
        form.save()
        return redirect("record_list")
    else:
        form = VerbalAutopsyForm()
        
    return render(request, "va/add_record.html", {"form": form})