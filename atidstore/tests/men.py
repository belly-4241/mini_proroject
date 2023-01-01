import time

import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def test_men():
    ser = Service(r"C:/Users/Asus/Downloads/chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(service=ser)
    driver.get("https://atid.store")
    time.sleep(3)
    driver.maximize_window()
    driver.find_element(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//h2[contains(text(),'Black Hoodie')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[contains(text(),'Add to cart')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div[1]/div[1]/a[1]").click()
    time.sleep(2)
    tes = driver.find_element(By.XPATH, "//a[contains(text(),'Green Hoodie')]").text
    assert tes == 'Green Hoodie'
    coupon_field=driver.find_element(By.XPATH,"//input[@id='coupon_code']")
    coupon_field.clear()
    sleep(2)
    coupon_field.send_keys('dfghjkl')
    sleep(2)
    driver.find_element(By.XPATH,"//button[contains(text(),'Apply coupon')]").click()
    sleep(3)





test_men()