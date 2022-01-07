from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome(r"C:\Users\Egidijus\Desktop\chromedriver.exe")

driver.get('https://csgo500.com/')

driver.implicitly_wait(3)

termsLabel = driver.find_element(By.XPATH, '//*[@id="login-content"]/div[3]/div/form/p[1]/label').click()
ageLabel = driver.find_element(By.XPATH, '//*[@id="login-content"]/div[3]/div/form/p[2]/label').click()
residentLabel = driver.find_element(By.XPATH, '//*[@id="login-content"]/div[3]/div/form/p[3]/label').click()

driver.implicitly_wait(3)

loginHover = driver.find_element(By.XPATH, '//*[@id="content-login"]')

hovering = ActionChains(driver).move_to_element(loginHover)
hovering.click().perform()

time.sleep(30)

divsPresence = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="past-queue-wrapper"]'))
)



while True:

    hashValue1 = driver.find_element(By.XPATH, '//*[@id="hash"]').text
    print(hashValue1)
    divs = driver.find_elements(By.XPATH, '//*[@id="past-queue-wrapper"]/div')

    results = []

    for c in divs:
        results.append(c.get_attribute('class')[5])

    lastResults = results[-32:]
    print(lastResults)

    loseStreak = 0

    for j in range(len(lastResults)):
        if lastResults[j] != '2':
            loseStreak += 1
        else:
            loseStreak = 0
    print(loseStreak)

    if loseStreak >= 8:
        bank = 100000
        initialBet = 30
        loseStreakForBlueBet = 0
        if lastResults[-1:] == '2':
            bank += initialBet * 5
            loseStreakForBlueBet = 0
            initialBet = 30
            print(bank)
        elif lastResults[-1:] != '2' and loseStreakForBlueBet == 0:
            bank -= initialBet
            initialBet = initialBet * 1.25
            loseStreakForBlueBet += 1
            print(bank)
        else:
            bank -= initialBet
            initialBet = initialBet * 1.25
            loseStreakForBlueBet += 1
            print(bank)

    while True:

        hashValue2 = driver.find_element(By.XPATH, '//*[@id="hash"]').text

        if hashValue1 == hashValue2:
            continue
        else:
            break

