from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.CLASS_NAME, "sort-icon").click()

correct_list = ['Almond', 'Apple', 'Banana', 'Beans', 'Brinjal']
list = []

list_of_elements = driver.find_elements(By.XPATH, "//tbody/tr/td[1]")
for i in list_of_elements:
    list.append(i.text)

assert correct_list == list
