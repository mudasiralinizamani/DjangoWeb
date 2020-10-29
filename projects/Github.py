import requests
from pprint import pprint
from  github import  Github

url =  f'https://api.github.com/users/DevonCrawford'
User_data = requests.get(url).json()
url2 =  f'https://api.github.com/repos/DevonCrawford/A-Pathfinding-Visualization'



Username = 'mudasiralinizamani'

Git = Github(Username,  'minemine123@')

User = Git.get_user()

Repos = User.get_repos('DjangoWeb')

User_Image = User_data.get('avatar_url')
User_Name = User_data.get('name')

Repo_Data = requests.get(url2).json()

Repo1_Desc = Repo_Data.get('description')
Repo1_url = Repo_Data.get('html_url')


PathFindingRepo  = User.get_repos()

pprint(Repo_Data)
