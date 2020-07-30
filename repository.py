from urllib.parse import urlparse


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
