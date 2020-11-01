import requests
from pprint import pprint
from  github import  Github

url = 'https://api.github.com/repos/DevonCrawford/YouTube-Descriptions-Updater'

langurl = 'https://api.github.com/repos/DevonCrawford/YouTube-Descriptions-Updater/languages'

def Get_Repo_Data(url):
    Data = requests.get(url).json()
    return Data

def Get_Repo_Languages_Data(url):
    Data = requests.get(url).json().get('languages_url')
    Languages = list(requests.get(Data).json())
    Lang = ''
    for l in Languages:
        Lang += f'{l}, '
    return Lang



