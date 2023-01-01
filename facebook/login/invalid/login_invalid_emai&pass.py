import time
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import select
def incoreectpw():
    driver = webdriver.Chrome()
    driver.get("https://www.Facebook.com/")
    driver.maximize_window()
    time.sleep(1)
    fb_user = driver.find_element(By.NAME, "email")
    fb_user.send_keys("enat95@gmail.com")
    time.sleep(1)
    fb_password = driver.find_element(By.NAME, "pass")
    fb_password.send_keys("0503054242")
    time.sleep(1)
    driver.find_element(By.NAME, "login").click()
    time.sleep(5)
    Error_message = driver.find_element(By.XPATH,"//div[contains(text(),'Invalid username or password')]").text
    assert 'Invalid username or password' == Error_message
    sleep(5)
incoreectpw()