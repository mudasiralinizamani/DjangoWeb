import requests
from pprint import pprint
from  github import  Github

url =  f'https://api.github.com/users/DevonCrawford'
User_data = requests.get(url).json()
url2 =  f'https://api.github.com/repos/DevonCrawford/A-Pathfinding-Visualization'






def Get_Repo_Data(url):
    Data = requests.get(url).json()
    return Data


Repo_Data = Get_Repo_Data(url2)

