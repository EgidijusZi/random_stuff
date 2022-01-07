from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time
import csv

driver = webdriver.Chrome(r"C:\Users\Egidijus\Desktop\chromedriver.exe")

driver.get('https://csgo500.com/crash')

element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content-crash"]/div[1]/div[1]/div[2]'))
)

time.sleep(3)

driver.find_element(By.CSS_SELECTOR, '#content-crash > div.crash-loaded > div.row.crash-top-bar > div.col.s12.m6.l7 > a.crash-recent-history.redtext > i').click()

while True:

    time.sleep(3)

    crashes = driver.find_elements(By.XPATH, '/html/body/div[16]/div/div[2]/div[2]/table/tbody/tr')

    crash_numbers = []

    for c in crashes:
        crash_numbers.append(c.text.split(' ')[1])

    csv_file = open('output.csv', 'a')
    my_output = csv.writer(csv_file, delimiter=';', lineterminator='\n')

    for r in crash_numbers:
        my_output.writerow([r])

    hover = driver.find_element(By.XPATH, '//*[@id="modal-crash-history"]/div/div[2]/div[3]/button')
    
    time.sleep(2)

    hovering = ActionChains(driver).move_to_element(hover)
    hovering.click().perform()

    csv_file.close()
    #clickable_element = WebDriverWait(driver, 10).until(
        #EC.presence_of_element_located((By.CLASS_NAME, 'btn-toolbar history-older-entries')).click()
    #)