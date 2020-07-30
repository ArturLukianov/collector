import unittest

from search import search
from regex import telegram_token_regex
from repository import Repository


class TestRepository(unittest.TestCase):
    '''Test repository scanner'''

    def test_repository_creates_from_url(self):
        '''Test: repository creates from url'''
        repo = Repository(url="https://github.com/octocat/Hello-World")

        self.assertIsNotNone(repo)
        self.assertEqual(repo.owner, 'octocat')
        self.assertEqual(repo.name, 'Hello-World')
        self.assertEqual(repo.api_url, 'https://api.github.com/repos/octocat/Hello-World')


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
