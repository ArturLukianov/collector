import unittest

from search import search
from regex import telgram_token_regex


class TestRepository(unittest.TestCase):
    '''Test repository scanner'''
    pass


class TestRegex(unitest.TestCase):
    '''Test regexes'''

    def test_telegram_token_regex_matches(self):
        '''Test: test that valid telegram tokens match regex'''
        tokens = [
            '1169639777:AAFdGx-nzjj67VjVsUOtqiE_-rzQSax2CBw',
            '1282912519:AAE2gkIO8pKAsqRKCficQRNWcW0haM_7-7k',
            '1390356647:AAHpJP1BAunDZsGBhalIC6ncxVA5Ryz-jzs',
            '1070920408:AAF7DKGt824r1LGHsiA_7WbzLEAhl23DMWc',
        ]

        for token in tokens:
            self.assertIsNotNone(telegram_token_regex.match(token))

class TestRepositorySearch(unittest.TestCase):
    '''Test GitHub repository searcher'''

    def test_search_returns_not_empty_list(self):
        '''Test: search and find something'''
        result = search(q='Telegram', sort='updated', order='asc')

        self.assertNotEqual(len(result), 0)
