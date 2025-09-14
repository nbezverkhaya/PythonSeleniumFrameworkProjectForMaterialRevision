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

def test_fixture_demo(setup):
    print("Hallo")

def test_cross_browser(cross_browser):
    print(cross_browser)
