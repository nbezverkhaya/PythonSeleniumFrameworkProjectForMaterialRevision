import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID, "exampleCheck1").click()
# css selector - tagname[attribute='value']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys('Nataliia')
driver.find_element(By.XPATH, "//input[@value='Submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
driver.find_element(By.LINK_TEXT, "London QA Meetup @Rahul Shetty - Limited Seats! Book Now!").click()
assert "Success" in message

name = "Nataliia"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
alert.accept()

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver.get_screenshot_as_file("screenshot.png")









time.sleep(2)
