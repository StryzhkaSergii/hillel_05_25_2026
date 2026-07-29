import pytest

def test_empty(pre_post_conditions):
    print("test is going")
    print(pre_post_conditions)

@pytest.fixture
def pre_post_conditions():
    print("Pre conditions started")
    yield "fixture value returned"
    print("Post conditions started")