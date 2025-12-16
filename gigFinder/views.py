import json
from django.shortcuts import render
from gigFinder.data import GigGroup, GIG_GROUP_JSON_SCHEMA
from google import genai

# Create your views here.

def index(request):
    return render(request, 'gigFinder/main.html')

def search(request):
    searchQuery = request.GET.get('q')

    prompt = f"""
    Find shows or festivals where {searchQuery} are playing in the UK, grouped into related categories such as festivals, album tour, etc.
    There should only be one group marked as important.
    """

    client = genai.Client(api_key='')
    response = client.models.generate_content(
        model='gemini-2.5-flash-lite',
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_json_schema": GIG_GROUP_JSON_SCHEMA
        },
    )
    gigs_data = json.loads(response.text)
    gigs = [GigGroup.from_json_data(gig_data) for gig_data in gigs_data]
    return render(request, 'gigFinder/search.html', {'gigs': gigs})