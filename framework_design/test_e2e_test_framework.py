import time

from pageObjects.login_page import LoginPage


def test_e2e(browser_instance):
    driver = browser_instance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    login_page = LoginPage(driver)
    shop_page = login_page.login()
    shop_page.add_product_to_cart("Blackberry")
    checkout_page = shop_page.go_to_cart()
    time.sleep(1)
    checkout_page.checkout()
    checkout_page.enter_delivery_address("st", "Austria")
    checkout_page.validate_order()

    time.sleep(4)
