from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")
options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(options=options)

driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)