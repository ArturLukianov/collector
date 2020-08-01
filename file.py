import requests


class File:
    '''File in GitHub'''

    def __init__(self, raw_url, filename=None):
        '''Initialization'''
        self.raw_url = raw_url
        self.filename = filename

        self.is_loaded = False

    def read(self):
        '''Read contents of file'''
        if self.is_loaded:
            return self.contents

        response = requests.get(self.raw_url)

        self.contents = response.content
        try:
            self.contents = self.contents.decode('utf8')
        except UnicodeError:
            self.contents = ''

        return self.contents
        
