import requests
import json


class GitHubAPI():
    '''GitHub API client'''

    github_api = "https://api.github.com"

    def __init__(self):
        '''Initialization'''
        self.username = None
        self.password = None

        self.is_authenticated = False

    def get(self, method, **kwargs):
        '''Do a get request to GitHub API'''
        url = self.github_api + method

        if self.is_authenticated:
            response = requests.get(url, auth=self.auth, **kwargs)
        else:
            response = requests.get(url, **kwargs)

        if response.status_code != 200:
            raise Exception("GitHub API returned non-successful status code")

        return response.json()

    def load_credentials(self, creds_file):
        '''Load credentials from file in json format'''
        with open(creds_file) as f:
            credentials = json.loads(f.read())

            self.username = credentials.get('username')
            self.password = credentials.get('password')

    def authenticate(self):
        '''Authenticate via basic authentication on server'''
        if self.is_authenticated:
            return True

        if self.username is not None and\
           self.password is not None:
            self.is_authenticated = True
            self.auth = (self.username, self.password)
            return True

        return False
