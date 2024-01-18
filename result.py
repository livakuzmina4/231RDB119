import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://www.ryanair.com/lv/en"
driver.get(url)
time.sleep(2)

find_destination = driver.find_element(By.XPATH, '//div[contains(@class, "input-button__departure")]')
input.send_keys("Riga")
time.sleep(1)

find_departure = driver.find_element(By.XPATH, '//div[contains(@class,"input-button__destination")]')
input.send_keys("Aarhus")
time.sleep(1)

date_picker = driver.find_element(By.XPATH, "//div[@data-id='flight-date-picker__depart-input']")
date_picker.click()
date_option = driver.find_element(By.XPATH, "//div[@data-id='flight-date-picker__desktop-day-15']")
date_option.click()

search_button = driver.find_element(By.XPATH, "//button[@data-ref='flight-search-widget__cta']")
search_button.click()
