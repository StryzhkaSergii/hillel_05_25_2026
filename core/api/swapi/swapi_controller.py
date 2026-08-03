import requests

from core.api.basic_controller import BasicController


class SwapiController(BasicController):
    def __init__(self, url="https://swapi.info/api/"):
        self.url = url

    def get_person(self, person_id):
        """
        send request to get /api/people/person_id
        :param person_id:
        :return:
        """
        url = f"{self.url}people/{person_id}"

        # if page is not None:
        #     url = url + "?page=" + page

        return self._execute_request("get", url=url)

    def get_people(self, params = None):
        url = f"{self.url}people"

        return self._execute_request(method= "get", url=url, params=params)