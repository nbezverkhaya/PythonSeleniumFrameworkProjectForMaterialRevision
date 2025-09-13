import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/upload-download-test/")
driver.find_element(By.ID, "downloadButton").click()

file_input = driver.find_element(By.ID, "fileinput")
file_input.send_keys("/Users/natulik/Downloads/download.xlsx")

wait = WebDriverWait(driver, 5)
toast_locator = (By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")
wait.until(expected_conditions.visibility_of_element_located(toast_locator))
confirmation_notice = driver.find_element(*toast_locator).text
assert confirmation_notice == "Updated Excel Data Successfully."

time.sleep(5)