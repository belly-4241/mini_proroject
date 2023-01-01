import time
from selenium import webdriver
from time import sleep
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
def test_women():
    ser = Service(r"C:/Users/Asus/Downloads/chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(service=ser)
    driver.get("https://atid.store")
    time.sleep(3)
    driver.maximize_window()
    driver.find_element(By.XPATH, "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[4]/a[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//h2[contains(text(),'Anchor Bracelet')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div[1]/div[1]/a[1]").click()
    time.sleep(3)
    bel = driver.find_element(By.XPATH,"//a[contains(text(),'Anchor Bracelet')]").text
    assert bel == 'Anchor Bracelet'
    time.sleep(3)

#test_women()





