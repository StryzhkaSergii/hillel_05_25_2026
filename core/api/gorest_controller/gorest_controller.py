import requests

from core.api.basic_controller import BasicController


class GorestController(BasicController):
    def __init__(self, url="https://gorest.co.in/public/v2/"):
        self.url = url
        self.token = self.get_token()

    def get_token(self):
        # тут може бути логіка логіну
        return "19ed479ee907709b391a0315fdfed5e1756f6a8fb607913415413b6c4a7a9c1d"

    def get_user(self, person_id, params=None):
        f"""
        send request to get /api/people/person_id
        :param person_id:
        :return:
        """
        url = f"{self.url}people/{person_id}"

        # if page is not None:
        #     url = url + "?page=" + page

        return requests.get(url=url, params=None)

    def get_users(self, params = None):
        url = f"{self.url}people"

        return requests.get(url=url, params=params)

    def create_user(self, data):
        url = f"{self.url}users"

        return self._execute_request(method="post", url=url, data=data,
                                     headers={"Authorization": f"Bearer {self.token}"})