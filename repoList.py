import requests

API = 'https://api.github.com/'


def repos():

    endpoint = "users/anuditnagar/repos"

    resp = requests.get(API + endpoint)
    data = resp.json()

    repoList = []
    for repo in data:
        print()
        repoList.append([repo['name'], repo['description'], repo['html_url'], repo['private'], f"https://github.com/{repo['full_name']}/archive/master.zip"])

    return repoList

print(repos())
