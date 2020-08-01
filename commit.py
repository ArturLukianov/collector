import requests
from file import File
from githubapi import GitHubAPI


class Commit:
    '''Commit made to repository'''

    def __init__(self, repo, sha, api=None):
        '''Initialize commit'''
        self.repo = repo
        self.sha = sha
        self.api_method = self.repo.api_method + '/commits/' + sha

        if api is None:
            self.api = GitHubAPI()
        else:
            self.api = api
        
        self.init_info()

    def init_info(self):
        '''Fetch primary info from GitHub'''
        result = self.api.get(self.api_method)

        self.message = result['commit']['message']

    def get_files(self):
        '''Fetch files associated with commit'''
        result = self.api.get(self.api_method)

        files = []

        for file_ in result['files']:
            files.append(File(
                raw_url=file_['raw_url'],
                filename=file_['filename']
            ))
        return files
