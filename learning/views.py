from pathlib import Path

from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render


def home(request):
    return render(request, 'learning/home.html')


def science(request):
    return render(request, 'learning/science.html')


def solar_system(request):
    simulator_file = Path(settings.BASE_DIR) / 'Solar_System.html'
    return FileResponse(simulator_file.open('rb'), content_type='text/html')

# Create your views here.
