import time
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import select
def loin():
    ser = Service(r"C:/Users/Asus/Downloads/chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(service=ser)
    driver.maximize_window()
    driver.get("https://facebook.com")
    time.sleep(3)
    driver.find_element(By.ID,"email").send_keys("")
    time.sleep(3)
    driver.find_element(By.ID,"pass").send_keys("")
    time.sleep(3)
    driver.find_element(By.NAME,"login").click()
    time.sleep(3)
    ema=driver.find_element(By.XPATH,"//div[contains(text(),'Invalid username or password')]").text
    assert ema=='Invalid username or password'



loin()
