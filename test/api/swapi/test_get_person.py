import unittest

from core.api.swapi.swapi_controller import SwapiController


swapi_controller = SwapiController()
class TestPerson(unittest.TestCase):

    def test_get_person(self):
        person_id = 2
        response = swapi_controller.get_person(person_id)

        self.assertEqual(200, response.status_code)

    def test_get_people_with_params(self):
        response = swapi_controller.get_people(params = {"page": 1})

        self.assertEqual(200, response.status_code)

    def test_get_people(self):
        response = swapi_controller.get_people()

        self.assertEqual(200, response.status_code)