import pytest


@pytest.fixture()
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")