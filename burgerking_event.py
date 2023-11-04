import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

time.sleep(3)

chrome_options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
url = 'https://www.burgerkingevent.com/?utm_medium=kakao_da&utm_source=cpc&utm_campaign=quattromaximum'
driver.get(url)
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div/img[2]').click()
time.sleep(5)

for i in range(1, 6):
    if 'btn_1_1.png' in driver.find_element(By.XPATH, f'//*[@id="play"]/div[2]/div[2]/div/div[2]/div[{i}]').get_attribute("innerHTML"):
        화 = driver.find_element(By.XPATH, f'//*[@id="play"]/div[2]/div[2]/div/div[2]/div[{i}]')
    elif 'btn_4_1.png' in driver.find_element(By.XPATH, f'//*[@id="play"]/div[2]/div[2]/div/div[2]/div[{i}]').get_attribute("innerHTML"):
        와 = driver.find_element(By.XPATH, f'//*[@id="play"]/div[2]/div[2]/div/div[2]/div[{i}]')
    elif 'btn_2_1.png' in driver.find_element(By.XPATH, f'//*[@id="play"]/div[2]/div[2]/div/div[2]/div[{i}]').get_attribute("innerHTML"):
        양 = driver.find_element(By.XPATH, f'//*[@id="play"]/div[2]/div[2]/div/div[2]/div[{i}]')
    elif 'btn_3_1.png' in driver.find_element(By.XPATH, f'//*[@id="play"]/div[2]/div[2]/div/div[2]/div[{i}]').get_attribute("innerHTML"):
        피 = driver.find_element(By.XPATH, f'//*[@id="play"]/div[2]/div[2]/div/div[2]/div[{i}]')
    elif 'btn_5_1.png' in driver.find_element(By.XPATH, f'//*[@id="play"]/div[2]/div[2]/div/div[2]/div[{i}]').get_attribute("innerHTML"):
        블 = driver.find_element(By.XPATH, f'//*[@id="play"]/div[2]/div[2]/div/div[2]/div[{i}]')

블.click()
양.click()
양.click()
블.click()
피.click()
화.click()
와.click()
와.click()
화.click()
와.click()
와.click()
화.click()
블.click()