from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import random
import time

driver = webdriver.Chrome("/Users/junotsang/Library/CloudStorage/OneDrive-HKUSTConnect/ust/academic/Yr4 Spring/IEDA 4200/Project/googleform_filler/chromedriver")

url = "https://docs.google.com/forms/d/e/1FAIpQLSeTAmGzdYVqv_kxEmHQqjXMK2ZNzpzP0qDpk-xtKl3PhtWHxg/viewform?usp=sf_link"

driver.get(url)

station = {
    "1":'//*[@id="i5"]/div[3]/div',
    "2":'//*[@id="i8"]/div[3]/div',
    "3":'//*[@id="i11"]/div[3]/div',
    '4':'//*[@id="i14"]/div[3]/div', 
    '5':'//*[@id="i17"]/div[3]/div',
    '6':'//*[@id="i20"]/div[3]/div',
    '7':'//*[@id="i23"]/div[3]/div',
    '8':'//*[@id="i26"]/div[3]/div',
    '9':'//*[@id="i29"]/div[3]/div',
    '10':'//*[@id="i32"]/div[3]/div',
    '11':'//*[@id="i35"]/div[3]/div',
    '12':'//*[@id="i38"]/div[3]/div',
    '13':'//*[@id="i41"]/div[3]/div',
    '14':'//*[@id="i44"]/div[3]/div',
    '15':'//*[@id="i47"]/div[3]/div'
}

eat = {
    "1":'//*[@id="i54"]/div[3]/div',
    "2":'//*[@id="i57"]/div[3]/div'
}

build = {
    '1':'//*[@id="i64"]/div[3]/div',
    '2':'//*[@id="i67"]/div[3]/div'
}

def fill_form():
    #Station
    button = random.choice(['1', '1', '1', '2', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '4', '4', '5', '5', '5', '5', '5', '5', '5', '5', '5', '6', '6', '7', '8', '9', '9', '9', '10', '10', '11', '12', '13', '14', '15'])
    choice = station[button]
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, choice)))
    driver.find_element_by_xpath(choice).click()

    #Wanna eat?
    button = random.choice(['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1','2'])
    choice = eat[button]
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, choice)))
    driver.find_element_by_xpath(choice).click()

    #Wanna build?
    button = random.choice(['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1','2'])
    choice = build[button]
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, choice)))
    driver.find_element_by_xpath(choice).click()

    #next
    WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span')))
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span').click()


for i in range(3):
    driver.implicitly_wait(15)
    fill_form()
    driver.implicitly_wait(15)
    driver.implicitly_wait(2)
    WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')))
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
