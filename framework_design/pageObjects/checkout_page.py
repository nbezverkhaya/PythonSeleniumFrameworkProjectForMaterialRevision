import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_btn = (By.CSS_SELECTOR, ".btn.btn-success")
        self.country_input = (By.ID, "country")
        self.checkout_btn2 = (By.CLASS_NAME, "checkbox-primary")
        self.purchase_btn = (By.CSS_SELECTOR, "input[value='Purchase']")
        self.alert_message = (By.CLASS_NAME, "alert-success")


    def checkout(self):
        time.sleep(1)
        self.driver.find_element(*self.checkout_btn).click()

    def enter_delivery_address(self, country_query, country):
        self.driver.find_element(*self.country_input).send_keys(country_query)
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, country)))
        self.driver.find_element(By.LINK_TEXT, country).click()
        self.driver.find_element(*self.checkout_btn2).click()
        self.driver.find_element(*self.purchase_btn).click()

    def validate_order(self):
        confirmation_text = self.driver.find_element(*self.alert_message).text
        assert "Success! Thank you!" in confirmation_text