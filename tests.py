import unittest

from search import search
from regex import telegram_token_regex
from repository import Repository
from commit import Commit
from file import File
from githubapi import GitHubAPI


class TestGitHubAPI(unittest.TestCase):
    '''Test GitHub API client'''

    def test_get_requests(self):
        '''Test: get and post requests to GitHub API'''
        api = GitHubAPI()

        response = api.get("/rate_limit")

        if response.status_code != 200:
            self.fail("Response status code is not successful")

        rate = response.json().get('rate')
        self.assertIsNotNone(rate)

    def test_github_authentication(self):
        '''Test: GitHub API client can authenticate on server'''
        api = GitHubAPI()

        username, password = api.load_credentials()

        api.authenticate(username=username, password=password)
    

class TestRepository(unittest.TestCase):
    '''Test repository scanner'''

    def test_repository_creates_from_url(self):
        '''Test: repository creates from url'''
        repo = Repository(url="https://github.com/octocat/Hello-World")

        self.assertIsNotNone(repo)
        self.assertEqual(repo.owner, 'octocat')
        self.assertEqual(repo.name, 'Hello-World')
        self.assertEqual(repo.api_url, 'https://api.github.com/repos/octocat/Hello-World')

    def test_repository_can_get_commits(self):
        '''Test: can get commits from repository'''
        repo = Repository(url="https://github.com/octocat/Hello-World")

        commits = repo.get_commits()

        self.assertNotEqual(len(commits), 0)

        for commit in commits:
            self.assertEqual(type(commit), Commit)


class TestCommit(unittest.TestCase):
    '''Test commits'''

    def test_commit_get_files(self):
        repo = Repository(url="https://github.com/octocat/Hello-World")
        commits = repo.get_commits()

        files = commits[0].get_files()

        self.assertNotEqual(len(files), 0)

        for file_ in files:
            self.assertEqual(type(file_), File)


class TestFile(unittest.TestCase):
    '''Test files attached to commits'''

    pass
            

class TestRegex(unittest.TestCase):
    '''Test regexes'''

    def test_telegram_token_regex_matches(self):
        '''Test: valid telegram tokens match regex'''
        tokens = [
            '1169639777:AAFdGx-nzjj67VjVsUOtqiE_-rzQSax2CBw',
            '1282912519:AAE2gkIO8pKAsqRKCficQRNWcW0haM_7-7k',
            '1390356647:AAHpJP1BAunDZsGBhalIC6ncxVA5Ryz-jzs',
            '1070920408:AAF7DKGt824r1LGHsiA_7WbzLEAhl23DMWc',
            '644739147:AAGMPo-Jz3mKRnHRTnrPEDi7jUF1vqNOD5k'
        ]

        for token in tokens:
            self.assertIsNotNone(
                telegram_token_regex.match(token),
                f'"{token}" not matches'
                )

    def test_telegram_token_regex_not_matches(self):
        '''Test: invalid telegram tokens do not match regex'''
        invalid_tokens = [
            'token',
            'if 1293021 is token:',
            'asdfasfasfd:asdfafafasdf',
            '1312313131312313'
        ]

        for invalid_token in invalid_tokens:
            self.assertIsNone(telegram_token_regex.match(invalid_token))

class TestRepositorySearch(unittest.TestCase):
    '''Test GitHub repository searcher'''

    def test_search_returns_not_empty_list(self):
        '''Test: search and find something'''
        result = search(q='Telegram', sort='updated', order='asc')

        self.assertNotEqual(len(result), 0)

    def test_search_returns_empty_list(self):
        '''Test: search returns empty list for bad query'''
        result = search(q='aldf908dsfhnhuyn9qc60qcinyr9c')

        self.assertEqual(len(result), 0)

    def test_search_returns_repositories(self):
        '''Test: search returns list of Repository objects'''
        result = search(q='Telegram')

        for repo in result:
            self.assertEqual(type(repo), Repository)


if __name__ == "__main__":
    unittest.main()
