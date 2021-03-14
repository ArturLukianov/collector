"""Parse GitHub search results for juicy info"""

from repository import Repository
from search import search
from regex import telegram_token_regex
from githubapi import GitHubAPI

credentials_file = "credentials.json"
save_file = "tg_tokens.txt"

query = "Telegram"
regex = telegram_token_regex

forbidden_prefixes = [
    "venv/",
    ".gitignore",
    ".github",
    ".idea"
]

forbidden_suffixes = [
    ".pyc",
    ".png",
    ".jpg",
    ".jpeg",
    ".svg"
]

print("-- [GitHub scanner] --", end="\n\n")

api = GitHubAPI()

print("Loading credentials from ", credentials_file)

api.load_credentials(credentials_file)
api.authenticate()

print("Search query:", query)
print("Regex:", regex)

repositories = search(q=query, sort="updated", order="desc", api=api)

print("Found", len(repositories), "repos")

save = open(save_file, "w")

gathered = []

for repo in repositories:
    print("Scanning", repo.owner + "/" + repo.name)
    # Fetch all commits from repository
    commits = repo.get_commits()
    for commit in commits:
        # Iterate over files changed by commits and scan them with regex
        print("Commit", commit.sha)
        files = commit.get_files()
        for file_ in files:
            # It's better to skip files with some extensions and in some directories
            skip = False
            for el in forbidden_prefixes:
                if file_.filename.startswith(el):
                    skip = True
                    break
            for el in forbidden_suffixes:
                if file_.filename.endswith(el):
                    skip = True
                    break

            if skip:
                print("Skip", file_.filename)
                continue
            
            print("File", file_.filename)
            results = regex.findall(file_.read())
            save.writelines([line + "\n" for line in results])
            save.flush()
            gathered += results
            if len(results) != 0:
                print('Found', len(results), 'potential tokens!')

print('-- Gathered info --')
print("\n".join(gathered))
print('-- END --')
save.close()
