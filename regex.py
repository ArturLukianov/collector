import re


telegram_token_regex = re.compile(r'[0-9]{7,10}:[a-zA-Z0-9_-]{35}')
