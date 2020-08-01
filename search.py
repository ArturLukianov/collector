import requests

from repository import Repository
from githubapi import GitHubAPI


def search(q=None, sort=None, order=None, api=None):
    '''Search github repos for query'''
    method = "/search/repositories"

    if api is None:
        api = GitHubAPI()

    data = dict()

    if q is not None: data['q'] = q
    if sort is not None: data['sort'] = sort
    if order is not None: data['order'] = order

    result = api.get(method, params=data)

    repos = []
    
    for item in result['items']:
        repos.append(Repository(item['html_url'], api=api))

    return repos
    
