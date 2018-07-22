from urllib.parse import urljoin
import requests, json


class AbstractApi(object):
    def __init__(self, base_path):
        self.base_path = base_path

    def _get(self, url):
        full_url = urljoin(self.base_path, url)
        print('base path:', self.base_path)
        print(full_url)
        response = requests.get(full_url)
        return self._error_handling(response)

    def _post(self, url, body):
        full_url = urljoin(self.base_path, url)
        response = requests.post(full_url, data=body)
        return self._error_handling(response)

    def _joint_path(self, path):
        return urljoin(self.base_path, path)

    def _error_handling(self, response):
        if response.ok:
            return response.json()
        else:
            error_text = 'Unexpected response status "{statuscode}"\n' \
                         'url: {url}\n' \
                         'header: {header}' \
                         'reason: {reason}'.format(statuscode=response.status_code,
                                                   url=response.url,
                                                   header=response.headers,
                                                   reason=response.reason)
            raise requests.HTTPError(error_text)
