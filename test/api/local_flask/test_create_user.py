import random

import requests
from faker import Faker

faker = Faker()

def test_create_user(flask_controller, sql_lite_cursor):
    score = random.randint(1,100)
    data = {"name":faker.name(), "score":score}

    row_response = flask_controller.create_student(data)
    response = row_response.json()

    assert row_response.status_code == 201
    assert response.get("id") is not None
    assert response.get("name") == data["name"]
    assert response.get("score") == score

    sql_lite_cursor.execute(f'''select id, name, score'''
                            f''' from student where id = {response.get('id')}''')

    user_id, user_name, user_score= sql_lite_cursor.fetchone()