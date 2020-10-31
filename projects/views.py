from django.shortcuts import render, redirect
from . import Github
from .models import GithubRepository
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def Projects(req):
    Gitrepo = GithubRepository.objects.all()
    Context = {'repo': Github.Repo_Data, 'db_repo':  Gitrepo}
    return render(req, 'Pages/Projects.html', Context)


def Post_repo(req):
    Repo_Context = {}
    if req.user.is_authenticated:
        if req.method == 'POST':
            Repo_Url = str(req.POST['add-repo'])
            if  'https://github.com/' in Repo_Url:
                Repo_Url = Repo_Url.replace('https://github.com/', 'https://api.github.com/repos/')
                Repo_data = Github.Get_Repo_Data(Repo_Url)
                Add_repo = GithubRepository(Repo_Name=Repo_data.get('name'), Repo_Url=Repo_data.get('html_url'), Repo_Desc=Repo_data.get('description'), Repo_Language=Repo_data.get('language'),  Repo_Createdat=Repo_data.get('created_at'), Repo_Size=Repo_data.get('forks_count'), Repo_Stars=Repo_data.get('stargazers_count'), Repo_OpenIssue=Repo_data.get('open_issues_count'), Repo_Owner_Url=Repo_data.get('owner').get('html_url'), Repo_Owner_Img=Repo_data.get('owner').get('avatar_url'), Repo_Owner_Name=Repo_data.get('owner').get('login'))
                Add_repo.save()
                Repo_Context = {'repo' :  Repo_data}
                return render(req, 'Projects/Repo.html', Repo_Context)
            else:
                return HttpResponse('Invalid URL')
    else:
        messages.error(req, 'You have to login to post a Repository')
        return redirect('Login')
        
    return render(req, 'Projects/Add_repo.html')
