from urllib.parse import urljoin
import requests, json


class AbstractApi(object):
    def __init__(self, base_path):
        self.base_path = base_path

    def _get(self, url):
        response = requests.get(url)
        return self._error_handling(response)

    def _post(self, url, body):
        response = requests.post(url, data=body)
        return self._error_handling(response)

    def _joint_path(self, path):
        return urljoin(self.base_path, path)

    def _error_handling(self, response):
        if response.ok:
            return resonse.json()
        else:
            error_text = 'Unexpected response status "{statuscode}"\n' \
                         'url: {url}\n' \
                         'header: {header}' \
                         'reason: {reason}'.format(statuscode=response.status_code,
                                                   url=response.url,
                                                   header=response.headers,
                                                   reason=response.reason)
            raise requests.HTTPError(error_text)
