from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import random
import time

driver = webdriver.Chrome("/Users/junotsang/Desktop/dev/googleform/chromedriver")

url = "https://docs.google.com/forms/d/e/1FAIpQLSeEVJr1_aPqm-l9Frjb29-KWoXOmPFXZMOsywKmLpCPXVnHnQ/viewform"

driver.get(url)

def fill_form():
    #Identity
    button = random.choice(['//*[@id="i5"]/div[3]/div', '//*[@id="i8"]/div[3]/div', '//*[@id="i11"]/div[3]/div/div'])
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, button)))
    driver.find_element_by_xpath(button).click()

    if button == '//*[@id="i5"]/div[3]/div':
        age = random.randint(18, 24)
    elif button == '//*[@id="i38"]/div[3]/div':
        age = random.randint(18, 50)
    else:
        age = random.randint(16, 50)

    #Gender
    button = random.choice(['//*[@id="i18"]/div[3]/div', '//*[@id="i21"]/div[3]/div', '//*[@id="i14"]/div[3]/div'])
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, button)))
    driver.find_element_by_xpath(button).click()

    #Age
    inputs = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    inputs.clear()
    inputs.send_keys(str(age))

    #Section
    # button = random.choice(['//*[@id="i35"]/div[3]/div', '//*[@id="i38"]/div[3]/div'])
    button = '//*[@id="i38"]/div[3]/div'
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, button)))
    driver.find_element_by_xpath(button).click()

    #next
    WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')))
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()


def page1():
    inputs = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[3]/div/div[1]/div/div[1]/input')
    inputs.clear()
    inputs.send_keys(str(random.randint(10, 30)))
    
    inputs = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[3]/div/div[1]/div/div[1]/input')
    inputs.clear()
    inputs.send_keys(str(random.randint(3, 9)))
    
    inputs = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[3]/div/div[1]/div/div[1]/input')
    inputs.clear()
    inputs.send_keys(str(random.randint(20, 40)))
    
    inputs = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[3]/div/div[1]/div/div[1]/input')
    inputs.clear()
    inputs.send_keys(str(random.randint(3, 10)))
    
    inputs = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[3]/div/div[1]/div/div[1]/input')
    inputs.clear()
    inputs.send_keys(str(random.randint(4, 10)))
    
    inputs = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[3]/div/div[1]/div/div[1]/input')
    inputs.clear()
    inputs.send_keys(str(random.randint(10, 40)))
    
    inputs = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[3]/div/div[1]/div/div[1]/input')
    inputs.clear()
    inputs.send_keys(str(random.randint(4, 15)))
    
    inputs = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[3]/div/div[1]/div/div[1]/input')
    inputs.clear()
    inputs.send_keys(str(random.randint(10, 50)))
    
    inputs = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[3]/div/div[1]/div/div[1]/input')
    inputs.clear()
    inputs.send_keys(str(random.randint(4, 20)))
    
    inputs = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[3]/div/div[1]/div/div[1]/input')
    inputs.clear()
    inputs.send_keys(str(random.randint(20, 40)))

    WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')))
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]').click()

def page2():
    inputs = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[3]/div/div[1]/div/div[1]/input')
    inputs.clear()
    inputs.send_keys(str(random.randint(10, 30)))
    
    inputs = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[3]/div/div[1]/div/div[1]/input')
    inputs.clear()
    inputs.send_keys(str(random.randint(3, 9)))
    
    inputs = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[3]/div/div[1]/div/div[1]/input')
    inputs.clear()
    inputs.send_keys(str(random.randint(20, 40)))
    
    inputs = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[3]/div/div[1]/div/div[1]/input')
    inputs.clear()
    inputs.send_keys(str(random.randint(3, 10)))
    
    inputs = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[3]/div/div[1]/div/div[1]/input')
    inputs.clear()
    inputs.send_keys(str(random.randint(4, 10)))
    
    inputs = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[3]/div/div[1]/div/div[1]/input')
    inputs.clear()
    inputs.send_keys(str(random.randint(10, 40)))
    
    inputs = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[3]/div/div[1]/div/div[1]/input')
    inputs.clear()
    inputs.send_keys(str(random.randint(4, 15)))
    
    inputs = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[3]/div/div[1]/div/div[1]/input')
    inputs.clear()
    inputs.send_keys(str(random.randint(10, 50)))
    
    inputs = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[3]/div/div[1]/div/div[1]/input')
    inputs.clear()
    inputs.send_keys(str(random.randint(4, 20)))
    
    inputs = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[3]/div/div[1]/div/div[1]/input')
    inputs.clear()
    inputs.send_keys(str(random.randint(20, 40)))

    WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')))
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]').click()

def lastpage():
    #Perishable
    button = random.choice(['//*[@id="i5"]/div[3]/div', '//*[@id="i8"]/div[3]/div'])
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, button)))
    driver.find_element_by_xpath(button).click()

    #Non-perishable
    button = random.choice(['//*[@id="i15"]/div[3]/div', '//*[@id="i18"]/div[3]/div'])
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, button)))
    driver.find_element_by_xpath(button).click()

    #Day 1
    button = random.choice(['//*[@id="i25"]/div[3]/div', '//*[@id="i28"]/div[3]/div', '//*[@id="i31"]/div[3]/div', '//*[@id="i34"]/div[3]/div', '//*[@id="i37"]/div[3]/div', '//*[@id="i40"]/div[3]/div'])
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, button)))
    driver.find_element_by_xpath(button).click()

    #Day 2
    button = random.choice(['//*[@id="i47"]/div[3]/div', '//*[@id="i50"]/div[3]/div', '//*[@id="i53"]/div[3]/div', '//*[@id="i56"]/div[3]/div', '//*[@id="i59"]/div[3]/div', '//*[@id="i62"]/div[3]/div'])
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, button)))
    driver.find_element_by_xpath(button).click()

    WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')))
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]').click()

for i in range(3):
    driver.implicitly_wait(15)
    fill_form()
    page1()
    page2()
    driver.implicitly_wait(15)
    lastpage()
    driver.implicitly_wait(2)
    WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')))
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
