import json
from pathlib import Path
from django.shortcuts import render
from gigFinder.data import GigGroup

# Create your views here.

def index(request):
    json_path = Path(__file__).parent / 'test-data.json'
    with open(json_path, 'r') as f:
        gigs_data = json.load(f)
    
    gigs = [GigGroup.from_json_data(gig_data) for gig_data in gigs_data]
    return render(request, 'gigFinder/main.html', {'gigs': gigs})