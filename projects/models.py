from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GithubRepository(models.Model):
    # repository_user_id = models.AutoField(null=True)
    repo_user = models.OneToOneField(User, on_delete=models.CASCADE)
    repo_name = models.CharField(max_length=100, default='')
    repo_url = models.CharField(max_length=300, default='')
    repo_desc = models.CharField(max_length=300, default='')
    repo_languages = models.CharField(max_length=50, default='')
    repo_createdat = models.CharField(max_length=30, default='')
    repo_forks = models.IntegerField(default=0)
    repo_size = models.IntegerField(default=0)
    repo_stars = models.IntegerField(default=0)
    repo_openissue = models.IntegerField(default=0)
    repo_owner_url = models.CharField(max_length=200, default='')
    repo_owner_img = models.CharField(max_length=300, default='')
    repo_owner_name = models.CharField(max_length=70, default='')
    repo_uploadedby_first_name = models.CharField(max_length=30, default='')
    repo_uploadedby_last_name = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.repo_name