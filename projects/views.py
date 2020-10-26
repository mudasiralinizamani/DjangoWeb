from django.shortcuts import render

# Create your views here.

def Projects(req):
    return render(req, 'Pages/Projects.html')