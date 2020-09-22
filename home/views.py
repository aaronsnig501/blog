from django.shortcuts import render

# Create your views here.
def index(request):
    """Index view

    Returns the index.html page
    """
    return render(request, "index.html")