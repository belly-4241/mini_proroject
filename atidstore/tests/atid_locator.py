Atid='https://atid.store/'
Accsosery="//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[5]/a[1]"
select="//body/div[@id='page']/div[@id='content']/div[1]/div[2]/main[1]/div[1]/ul[1]/li[2]/div[2]/a[1]"
button="//button[contains(text(),'Add to cart')]"
cartSelect="//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/a[1]"
CartAdd="//h1[contains(text(),'Cart')]"
AmoutSelect="//input[@id='coupon_code']"
S_loketer="//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]"
S_mane="//body/div[@id='page']/div[@id='content']/div[1]/div[2]/main[1]/div[1]/ul[1]/li[1]/div[1]/a[1]"
S_button="//button[contains(text(),'Add to cart')]"
S_selector="//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div[1]/div[1]/a[1]"
S_Addcart="//a[contains(text(),'Anchor Bracelet')]"
S_chek="//input[@id='coupon_code']"
Women="//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[4]/a[1]"
W_select="//h2[contains(text(),'Anchor Bracelet')]"
W_cart="//button[contains(text(),'Add to cart')]"
W_addcart="//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div[1]/div[1]/a[1]/div[1]/span[1]"
W_button="//a[contains(text(),'Anchor Bracelet')]"
W_chek="//input[@id='coupon_code']"

Mane="//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]"
M_select="//body/div[@id='page']/div[@id='content']/div[1]/div[2]/main[1]/div[1]/ul[1]/li[3]/div[1]/a[1]/img[1]"
M_addCart="//button[contains(text(),'Add to cart')]"
M_check="//a[contains(text(),'ATID Green Tshirt')]"
M_input="//input[@id='coupon_code']"
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from atidloketor import *

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