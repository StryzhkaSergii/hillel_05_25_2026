import requests



def test_get_students(base_url):
    response = requests.get(url=f"{base_url}/students/").json()

    assert response != []
    assert len(set([k["id"] for k in response])) == len(response)

def test_get_first_student(base_url):
    response = requests.get(url=f"{base_url}/students/1").json()

    assert isinstance(response, dict)
    assert response["id"] == 1