import json

import pytest

from pageObjects.login_page import LoginPage

test_data_path ='../framework_design/data/test_e2e.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browser_instance, test_list_item):
    driver = browser_instance
    login_page = LoginPage(driver)
    shop_page = login_page.login(test_list_item["userEmail"], test_list_item["userPassword"])
    shop_page.add_product_to_cart(test_list_item["productName"])
    checkout_page = shop_page.go_to_cart()
    checkout_page.checkout()
    checkout_page.enter_delivery_address(test_list_item["country_query"], test_list_item["country"])
    checkout_page.validate_order()
