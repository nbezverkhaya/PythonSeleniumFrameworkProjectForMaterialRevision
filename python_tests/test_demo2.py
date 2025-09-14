import pytest


# @pytest.mark.smoke
@pytest.mark.xfail
def test_first_program():
    msg = "Hallo"
    assert "Hi" in msg
#
# @pytest.mark.skip
def test_second_credit_card():
    a = 4
    b = 6
    assert a + 2 == b

@pytest.fixture()
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")

def test_fixture_demo(setup):
    print("Hallo")