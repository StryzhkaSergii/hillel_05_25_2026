from settings import settings
from core.api.basic_controller import BasicController


class LocalFlaskController(BasicController):

    __headers = None

    def __init__(self, url=settings.LOCAL_FLASK_URL):
        self.url = url
        self.auth()

    def auth(self):
        url = f"{self.url}/auth/"
        name = settings.LOCAL_FLASK_NAME
        password = settings.LOCAL_FLASK_PASSWORD
        response = self._execute_request(method="post", url=url, json={"name":name, "password":password}).text
        __class__.__headers = {"token":response}

    def create_student(self, json_body: dict):
        url = f"{self.url}/students/"

        return self._execute_request(method="post", url=url, json=json_body, headers=self.__headers)

    def get_student(self, id):
        url = f"{self.url}/students/{id}"

        return self._execute_request(method="get", url=url)