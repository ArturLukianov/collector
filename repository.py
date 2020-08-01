import requests
from urllib.parse import urlparse

from commit import Commit


github_api_url = "https://api.github.com"


class Repository:
    '''GitHub repository'''

    def __init__(self, url=None):
        '''Initialize repository'''
        if url is None:
            raise Exception("GitHub repository needs url to create")

        self.url = url

        path = urlparse(url).path.split('/')
        
        self.owner = path[1]
        self.name = path[2]

        self.api_url = github_api_url + "/repos" + urlparse(url).path

    def get_commits(self):
        '''Get all commits made to repository'''
        response = requests.get(self.api_url + '/commits')

        if response.status_code != 200:
            raise Exception("GitHub API returned not sucessful status code")

        result = response.json()

        commits = []

        for commit in result:
            commits.append(Commit(repo=self, sha=commit['sha']))

        return commits
