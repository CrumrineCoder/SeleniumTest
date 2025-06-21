from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

assert "Web form" in driver.title