from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def Profile(req):
    return render(req, 'accounts/Admin.html')