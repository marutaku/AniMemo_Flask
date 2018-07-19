import requests
import json
from lib import config


class AbstractDB(object):
    db_url = 'http://dbkiso.si.aoyama.ac.jp/jsonapi/'

    def _custom_json(self, sql):
        '''
        POSTリクエストに用いるBODYをJSON文字列で生成
        :return: str
        '''
        return {
            'userid': config.userid,
            'password': config.password,
            'db': config.db,
            'sql': sql
        }

    def _request(self, sql):
        post_body = self._custom_json(sql)
        res = requests.post(self.db_url, data=post_body)
        if res.status_code == 200:
            return self._check_error(json.loads(res.text))
        else:
            raise requests.HTTPError('Unexpected status code: {}'.format(res.status_code))

    def _check_error(self, res):
        '''
        {results: fail}でないかを確認
        :param res: dict
        :return: dict
        '''
        if res['result'] & res['result'] == 'fail':
            raise Exception('SQLError')
        return res
