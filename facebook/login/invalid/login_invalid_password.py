import time
#import pytest
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
    fb_user.send_keys("belly4241@gmail.com")
    time.sleep(1)
    fb_password = driver.find_element(By.NAME, "pass")
    fb_password.send_keys("passwerd124")
    time.sleep(1)
    driver.find_element(By.NAME, "login").click()
    time.sleep(1)
    Error_message = driver.find_element(By.XPATH,
                                        "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[2]").text
    assert 'Invalid username or password' == Error_message
    sleep(5)
incoreectpw()

