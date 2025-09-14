import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

wait = WebDriverWait(driver, 7)

driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

product_list = driver.find_elements(By.CSS_SELECTOR, ".card.h-100")
for prod in product_list:
    prod_name = prod.find_element(By.XPATH, "div/h4/a").text
    if prod_name == "Blackberry":
        prod.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,".btn.btn-success").click()
driver.find_element(By.ID, "country").send_keys("st")
wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Austria")))
driver.find_element(By.LINK_TEXT, "Austria").click()
driver.find_element(By.CLASS_NAME, "checkbox-primary").click()
driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']").click()
confirmation_text = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success! Thank you!" in confirmation_text







time.sleep(4)