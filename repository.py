import requests
from urllib.parse import urlparse

from githubapi import GitHubAPI
from commit import Commit


class Repository:
    '''GitHub repository'''

    def __init__(self, url=None, api=None):
        '''Initialize repository'''
        if url is None:
            raise Exception("GitHub repository needs url to create")

        self.url = url

        path = urlparse(url).path.split('/')
        
        self.owner = path[1]
        self.name = path[2]

        if api is None:
            self.api = GitHubAPI()
        else:
            self.api = api

        self.api_method = "/repos" + urlparse(url).path

    def get_commits(self):
        '''Get all commits made to repository'''
        result = self.api.get(self.api_method + '/commits')

        commits = []

        for commit in result:
            commits.append(Commit(repo=self, sha=commit['sha'], api=self.api))

        return commits
