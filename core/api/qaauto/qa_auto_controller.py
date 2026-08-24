from core.api.basic_controller import BasicController
from core.api.qaauto.schema_models.schema_get_user import CurrentSchema
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

    def get_current(self, use_cookies=True, check_schema=True):
        """
        send request to get /users/current
        """
        url = f"{self.url}/users/current"
        cookies = self.cookies if use_cookies else None
        response = self._execute_request(method="get", url=url, cookies=cookies)
        if check_schema:
            CurrentSchema().load(response.json())
        return response