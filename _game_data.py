from requests import get
from bs4 import BeautifulSoup
from datetime import date

_ID = str(date.today().year) + str(date.today().month) + str(date.today().day)

_SOUP = BeautifulSoup(get('https://twentyletters.com').text, 'html.parser')


def get_score():
    return int(_SOUP.find('div', id=_ID).get('data-score'))


def get_letters():
    return [x.lower() for x in _SOUP.find('div', id=_ID).contents[0].get_text()]
