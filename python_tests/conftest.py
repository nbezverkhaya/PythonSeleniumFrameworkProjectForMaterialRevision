import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")

@pytest.fixture()
def data_load():
    print("User profile data is being created")
    return ["Nataliia", "Kra", "rahulshettyacademy.com"]

@pytest.fixture(params=[("chrome", "Nataliia"), "firefox", "safari"])
def cross_browser(request):
    return request.param