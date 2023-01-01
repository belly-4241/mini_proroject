from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from atid_locator import *

def test_women():
    driver = webdriver.Chrome()
    driver.get(Atid)
    driver.maximize_window()
    sleep(3)
    driver.find_element(By.XPATH,Women).click()
    sleep(3)
    driver.find_element(By.XPATH,W_select).click()
    sleep(3)
    driver.find_element(By.XPATH,W_cart).click()
    sleep(3)
    driver.find_element(By.XPATH,).click()
    sleep(3)
    name=driver.find_element(By.XPATH,W_button).text
    assert name=="Anchor Bracelet"
    sleep(3)
    coupon_fiel=driver.find_element(By.XPATH,W_chek)
    coupon_fiel.clear()
    sleep(3)
    coupon_fiel.send_keys('1234w')
    sleep(3)
test_women()