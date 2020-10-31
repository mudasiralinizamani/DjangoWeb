from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GithubRepository(models.Model):
    Repo_Name = models.CharField(max_length=100)
    Repo_Url = models.CharField(max_length=300)
    Repo_Desc = models.CharField(max_length=300)
    Repo_Language = models.CharField(max_length=50)
    Repo_Createdat = models.CharField(max_length=30)
    Repo_Forks = models.IntegerField(default=0)
    Repo_Size = models.IntegerField(default=0)
    Repo_Stars = models.IntegerField(default=0)
    Repo_OpenIssue = models.IntegerField(default=0)
    Repo_Owner_Url = models.CharField(max_length=200)
    Repo_Owner_Img = models.CharField(max_length=300)
    Repo_Owner_Name = models.CharField(max_length=70)

    def __str__(self):
        return self.Repo_Name