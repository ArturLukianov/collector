import requests


github_api_url = "https://api.github.com"


def search(q=None, sort=None, order=None):
    '''Search github repos for query'''
    method = "/search/repositories"

    data = dict()

    if q is not None: data['q'] = q
    if sort is not None: data['sort'] = sort
    if order is not None: data['order'] = order

    response = requests.get(
        github_api_url + method,
        params=data
    )

    if response.status_code != 200:
        raise Exception(
            f"GitHub API returned not succes code: {response.status_code}"
            "----"
            f"{response.content}"
            "----"
            )

    result = response.json()

    repos = []
    
    for item in result['items']:
        repos.append(item['url'])

    return repos
    
