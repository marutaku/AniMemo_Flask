import requests, json
from urllib.parse import urljoin
from lib.api.AbstractAPI import AbstractApi


class ShangriLa(AbstractApi):
    def __init__(self):
        super(ShangriLa, self).__init__('http://api.moemoe.tokyo/anime/v1/master/')

    def get_cours(self):
        path = 'course'
        return self._get(path)

    def get_by_year(self, year):
        return self._get(year)

    def get_by_year_and_cours(self, year, cours):
        path = '{}/{}'.format(year, cours)
        return self._get(path)
