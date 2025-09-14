import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_first_program(self):
        print("Hallo")

    def test_second_program(self):
        print("Smth")

    def test_third_program(self):
        print("Bye")