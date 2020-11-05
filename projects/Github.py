import requests
from pprint import pprint

url = 'https://api.github.com/repos/DevonCrawford/YouTube-Dscriptions-Updater'

langurl = 'https://api.github.com/repos/DevonCrawford/YouTube-Descriptions-Updater/languages'

def Get_Repo_Data(url):
    Data = requests.get(url).json()
    Not_found = False
    if Data.get('message') == 'Not Found':
        Not_found = True
        return Not_found
    return Data

def Get_Repo_Languages_Data(url):
    Data = requests.get(url).json().get('languages_url')
    Languages = list(requests.get(Data).json())
    Lang = ''
    for l in Languages:
        Lang += f'{l}, '
    return Lang
