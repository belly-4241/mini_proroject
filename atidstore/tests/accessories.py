import time
import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
def test_accessories():
    ser = Service(r"C:/Users/Asus/Downloads/chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(service=ser)
    driver.get("https://atid.store")
    time.sleep(3)
    driver.maximize_window()
    driver.find_element(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[5]/a[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@id='wc-block-search__input-1']").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[contains(text(),'Filter')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//div[@id='woocommerce_price_filter-2']").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//h2[contains(text(),'Bright Red Bag')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[contains(text(),'Add to cart')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div[1]/div[1]/a[1]").click()
    time.sleep(3)
    acs = driver.find_element(By.XPATH,"//a[contains(text(),'Bright Red Bag')]").text
    assert acs=='Bright Red Bag'
    time.sleep(3)

test_accessories()
def test():
    print(test())

