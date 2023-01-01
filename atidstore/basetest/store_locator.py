from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from atid_locator import *

def test_store():
    driver = webdriver.Chrome()
    driver.get(Atid)
    driver.maximize_window()
    sleep(3)
    driver.find_element(By.XPATH,S_loketer).click()
    sleep(3)#
    driver.find_element(By.XPATH,S_mane).click()
    sleep(3)#
    driver.find_element(By.XPATH,S_button).click()
    sleep(3)
    driver.find_element(By.XPATH,S_selector).click()
    sleep(4)
    name = driver.find_element(By.XPATH, S_Addcart).text
    assert name == 'Anchor Bracelet'
    coupon_field=driver.find_element(By.XPATH,S_chek)
    sleep(3)
    coupon_field.clear()
    coupon_field.send_keys('2345rty')
    sleep(3)
test_store()