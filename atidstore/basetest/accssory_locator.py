from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from atid_locator import *

def test_accessorie():
    driver = webdriver.Chrome()
    driver.get(Atid)
    driver.maximize_window()
    sleep(3)
    driver.find_element(By.XPATH,Accsosery).click()

    sleep(3)
    driver.find_element(By.XPATH,select).click()
    sleep(3)
    driver.find_element(By.XPATH,button).click()
    sleep(3)
    driver.find_element(By.XPATH,cartSelect).click()
    sleep(3)
    bank=driver.find_element(By.XPATH,CartAdd).text
    assert bank=="Cart"
    sleep(3)
    coupon_field=driver.find_element(By.XPATH,AmoutSelect)
    coupon_field.clear()
    sleep(3)
    coupon_field.send_keys('dfghjkyu78')
    sleep(3)
    driver.close()

test_accessorie()