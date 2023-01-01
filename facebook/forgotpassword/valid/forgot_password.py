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
    driver.find_element(By.ID, "email").send_keys("belly4241@gmail.com")
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[3]/a[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@id='identify_email']").send_keys("belly4241@gmail.com")
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[@id='did_submit']").click()
    time.sleep(3)
    tes = driver.find_element(By.XPATH,"//div[contains(text(),'No Search Results')]").text
    assert tes == 'No Search Results'


forg()
