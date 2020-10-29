from django.shortcuts import render
from . import Github
from  django.http import HttpResponse

# Create your views here.

def Projects(req):
    Context = {'user1_image': Github.User_Image, 'user1_name':  Github.User_Name, 'repo1_desc': Github.Repo1_Desc,
                        'repo1_url': Github.Repo1_url, 'repo': Github.Repo_Data
                        }
    return render(req, 'Pages/Projects.html', Context)
