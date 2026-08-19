import pytest



@pytest.mark.qaauto_api
def test_get_current_positive(qa_auto_controller):
    response_current = qa_auto_controller.get_current()
    print(response_current.json())
    assert response_current.status_code == 200
    assert response_current.json()["status"] == "ok"