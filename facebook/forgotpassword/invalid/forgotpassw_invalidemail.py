import time
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import select


def forg():
    ser = Service(r"C:/Users/Asus/Downloads/chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(service=ser)
    driver.maximize_window()
    driver.get("https://facebook.com")
    time.sleep(3)
    driver.find_element(By.ID, "email").send_keys("belly@gmail.com")
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[3]/a[1]").click()
    time.sleep(3)
    we = driver.find_element(By.XPATH,"//div[contains(text(),'Please enter your email or mobile number to search')]").text
    assert we=='Please enter your email or mobile number to search'



forg()