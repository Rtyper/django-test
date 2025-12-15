import json
from pathlib import Path
from django.shortcuts import render

# Create your views here.

def index(request):
    json_path = Path(__file__).parent / 'test-data.json'
    with open(json_path, 'r') as f:
        gigs = json.load(f)
    
    return render(request, 'gigFinder/main.html', {'gigs': gigs})