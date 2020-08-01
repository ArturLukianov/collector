import requests
from file import File


class Commit:
    '''Commit made to repository'''

    def __init__(self, repo, sha):
        '''Initialize commit'''
        self.repo = repo
        self.sha = sha
        self.url = self.repo.api_url + '/commits/' + sha

        self.init_info()

    def init_info(self):
        '''Fetch primary info from GitHub'''
        response = requests.get(self.url)

        if response.status_code != 200:
            raise Exception("GitHub API returned not succesful status code")

        result = response.json()

        self.message = result['commit']['message']

    def get_files(self):
        '''Fetch files associated with commit'''
        response = requests.get(self.url)

        result = response.json()

        files = []

        for file_ in result['files']:
            files.append(File(
                raw_url=file_['raw_url'],
                filename=file_['filename']
            ))
        return files
