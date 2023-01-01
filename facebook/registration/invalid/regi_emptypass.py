import time
#import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import select


def reg():
    ser = Service(r"C:/Users/Asus/Downloads/chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(service=ser)
    driver.maximize_window()
    driver.get("https://facebook.com")
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[text()='Create New Account']").click()
    time.sleep(3)
    driver.find_element(By.NAME, "firstname").send_keys("belly")
    time.sleep(1)
    driver.find_element(By.NAME, "lastname").send_keys("take")
    time.sleep(1)
    driver.find_element(By.NAME, "reg_email__").send_keys("belly4241@gmail.com")
    time.sleep(1)
    driver.find_element(By.NAME, "reg_email_confirmation__").send_keys("")
    driver.find_element(By.ID, "password_step_input").send_keys("")
    time.sleep(1)
    driver.find_element(By.NAME, "birthday_day").send_keys("15")
    time.sleep(1)
    driver.find_element(By.NAME, "birthday_month").send_keys("August")
    time.sleep(1)
    driver.find_element(By.NAME, "birthday_year").send_keys("1990")
    time.sleep(1)
    driver.find_element(By.XPATH, "//label[contains(text(),'Male')]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()
    time.sleep(3)
    fna = driver.find_element(By.XPATH,"//div[@id='js_63s']").text
    assert fna == 'js_63s'

reg()