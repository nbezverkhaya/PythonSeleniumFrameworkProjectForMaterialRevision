from selenium.webdriver.common.by import By

from pageObjects.checkout_page import CheckoutPage

from utils.browser_utils import BrowserUtils


class ShopPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.product_list = (By.CSS_SELECTOR, ".card.h-100")
        self.checkout_btn =(By.CSS_SELECTOR, ".nav-link.btn.btn-primary")

    def add_product_to_cart(self, product_name):
        product_list = self.driver.find_elements(*self.product_list)
        for prod in product_list:
            prod_name = prod.find_element(By.XPATH, "div/h4/a").text
            if prod_name == product_name:
                prod.find_element(By.XPATH, "div/button").click()

    def go_to_cart(self):
        self.driver.find_element(*self.checkout_btn).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page