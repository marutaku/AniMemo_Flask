import requests
import json
from lib import config


class AbstractDB:
    db_url = 'http://dbkiso.si.aoyama.ac.jp/jsonapi/'

    def __init__(self):
        pass

    def _custom_json(self, sql):
        '''
        POSTリクエストに用いるBODYをJSON文字列で生成
        :return: str
        '''
        return {
            'userid': config.user,
            'password': config.password,
            'db': config.db,
            'sql': sql
        }

    def _request(self, sql):
        post_body = self._custom_json(sql)
        print('='*30)
        print('Request content: {}'.format(post_body))
        res = requests.post(self.db_url, data=post_body)
        print('=' * 30)
        print('Response content: {}'.format(res.text))
        print('=' * 30)
        if res.ok:
            return self._check_error(json.loads(res.text))
        else:
            raise requests.HTTPError('Unexpected status code: {}'.format(res.status_code))

    def _check_error(self, res):
        '''
        {results: fail}でないかを確認
        :param res: dict
        :return: dict
        '''
        if type(res) == 'dict' and res['result'] and res['result'] == 'fail':
            raise Exception('SQLError')
        return res
