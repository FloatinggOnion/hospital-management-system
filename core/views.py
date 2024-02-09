from django.shortcuts import render
from .models import Hospital
from hospital_management.schema import Query

def index(request):
    return render(request, 'index.html')

def hospital_list(request):
    hospitals = Query.resolve_all_hospitals(self=None, info=None)
    return render(request, 'hospitals.html', {'hospitals': hospitals})