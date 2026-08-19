from core.api.basic_controller import BasicController
from settings import settings

class QAAUTOController(BasicController):
    def __init__(self, url=settings.QA_AUTO_API_URL):
        self.url = url
        self.cookies = None

    def login(self, json=None):
        """
        send request to get /auth/signin
        """
        url = f"{self.url}/auth/signin"
        response = self._execute_request(method="post", url=url, json=json)
        self.cookies = dict(response.cookies)
        return response

    def get_current(self, use_cookies=True):
        """
        send request to get /users/current
        """
        url = f"{self.url}/users/current"
        cookies = self.cookies if use_cookies else None

        return self._execute_request(method="get", url=url, cookies=cookies)