from django.shortcuts import render, redirect
from . import Github
from .models import GithubRepository
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def Projects(req):
    Gitrepo = GithubRepository.objects.all()
    Context = {'db_repo':  Gitrepo}
    return render(req, 'Pages/Projects.html', Context)


def Post_repo(req):
    Repo_Context = {}
    Db_Repos = GithubRepository.objects.all()
    Repos = []
    # Adding all the repositories names into one list variable - Mudasir Ali
    for Repo in Db_Repos:
        Repos.append(Repo.repo_name)
    # Checking the user is Authenticated - Mudasir Ali
    if req.user.is_authenticated:
        # If the request is POST
        if req.method == 'POST':
            Repo_Url = str(req.POST['add-repo'])
            if  'https://github.com/' in Repo_Url:
                Repo_Url = Repo_Url.replace('https://github.com/', 'https://api.github.com/repos/')
                Repo_data = Github.Get_Repo_Data(Repo_Url)
                # Cheking the Repository is available or NOT
                if Repo_data == True:
                    messages.error(req, 'This Repository is not available, Plz insert another Repository url.')
                    return redirect('Post_Repo')
                Repo_Languages =  Github.Get_Repo_Languages_Data(Repo_Url)
                # Cheking if the repository is already uploaded to the website - Mudasir Ali
                if Repo_data.get('name') in Repos:
                    messages.error(req, 'This Repository is already available in our database')
                    return redirect('Post_Repo')
                else: 
                    # Adding the repository to the Database - Mudasir Ali
                    # Creating Variables for Adding to Database - Mudasir Ali
                    Repo_Name = Repo_data.get('name')
                    Repo_Url = Repo_data.get('html_url')
                    Repo_Desc = Repo_data.get('description')
                    Repo_Createdat = Repo_data.get('created_at')
                    Repo_Forks = Repo_data.get('forks_count')
                    Repo_Size = Repo_data.get('size')
                    Repo_Stars = Repo_data.get('stargazers_count')
                    Repo_Oppenissue = Repo_data.get('open_issues_count')
                    Repo_Owner = Repo_data.get('owner')
                    Repo_Owner_Name = Repo_Owner.get('login')
                    Repo_Owner_Img = Repo_Owner.get('avatar_url')
                    Repo_Owner_Url = Repo_Owner.get('html_url')
                    Repo_Uploadedby_Firstname = req.user.first_name
                    Repo_Uploaded_Lastname = req.user.last_name
                    # Adding data to Database - Mudasir Ali
                    Add_repo = GithubRepository(repo_name=Repo_Name, repo_url=Repo_Url, repo_desc=Repo_Desc, repo_languages=Repo_Languages, repo_createdat=Repo_Createdat, repo_forks=Repo_Forks, repo_size=Repo_Size, repo_stars=Repo_Stars, repo_openissue=Repo_Oppenissue, repo_owner_url=Repo_Owner_Url, repo_owner_img=Repo_Owner_Img, repo_owner_name=Repo_Owner_Name, repo_uploadedby_first_name=Repo_Uploadedby_Firstname, repo_uploadedby_last_name=Repo_Uploaded_Lastname)
                    Add_repo.save()
                    Repo_Context = {'repo' :  GithubRepository.objects.get(repo_name=Repo_Name)}
                    messages.info(req, 'This is How you Repository will look like.')
                    return render(req, 'Projects/Repo.html', Repo_Context)
            else:
                messages.error(req, 'Invalid Url')
                return redirect('Post_Repo')
    # If the user is not Authenticated - Mudasir Ali
    else:
        messages.error(req, 'You have to login to post a Repository')
        return redirect('Login')
        
    return render(req, 'Projects/Add_repo.html')
