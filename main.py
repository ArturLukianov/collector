"""Parse GitHub search results for juicy info"""

from repository import Repository
from search import search
from regex import telegram_token_regex
from githubapi import GitHubAPI

credentials_file = "credentials.json"
query = "Telegram"
regex = telegram_token_regex

print("-- [GitHub scanner] --", end="\n\n")

api = GitHubAPI()

print("Loading credentials from ", credentials_file)

api.load_credentials(credentials_file)
api.authenticate()

print("Search query:", query)
print("Regex:", regex)

repositories = search(q=query, sort="updated", order="desc", api=api)

print("Found", len(repositories), "repos")

gathered = []

for repo in repositories:
    print("Scanning", repo.owner + "/" + repo.name)
    commits = repo.get_commits()
    for commit in commits:
        print("Commit", commit.sha)
        files = commit.get_files()
        for file_ in files:
            print("File", file_.filename)
            results = regex.search(file_.read())
            if results is not None:
                print(results)
                input()
