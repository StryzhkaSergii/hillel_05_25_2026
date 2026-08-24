import pytest


@pytest.mark.parametrize("student_id", [5])
def test_get_student(flask_controller, student_id,):
    response = flask_controller.get_student(student_id).json()
    assert response["id"] == student_id