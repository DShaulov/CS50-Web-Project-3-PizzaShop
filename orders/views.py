"""
The module responsible for directing the user around the site?!
"""

from django.shortcuts import render
from .models import Salad

# Create your views here.
def index(request):
    """return the front page"""
    context = {
        "salads": Salad.objects.all()
    }
    return render(request, 'index.html', context=context)
