from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from atid_locator import *


def test_men():
    driver = webdriver.Chrome()
    driver.get(Atid)
    driver.maximize_window()
    driver.find_element(By.XPATH,Mane).click()
    sleep(3)
    driver.find_element(By.XPATH,M_select).click()
    sleep(3)
    driver.find_element(By.XPATH,M_addCart).click()
    sleep(3)
    driver.find_element(By.XPATH,M_button).click()
    sleep(3)
    atanaw=driver.find_element(By.XPATH,M_check).text
    sleep(3)
    assert atanaw=="ATID Green Tshirt"
    sleep(3)
    coupon_field=driver.find_element(By.XPATH,)
    sleep(3)
    coupon_field.clear()
    sleep(3)
    coupon_field.send_keys('345ert')
    sleep(3)
    driver.close()
test_men()