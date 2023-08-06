import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
browser = webdriver.Edge(executable_path = 'C:/Users/riyaa/edgedriver_win64/msedgedriver')
browser.get('https://www.mapdevelopers.com/distance_from_to.php')
browser.find_element(By.XPATH, "//input[contains(@id, 'fromInput-map-control')]").send_keys('Thapar Institute of Engineering and Technology, Patiala')
browser.find_element(By.XPATH, "//input[contains(@id, 'toInput-map-control')]").send_keys('250002, Meerut')
x = browser.find_elements(By.XPATH, "//button[contains(@id, ('calculate-distance-map-control'))]")[0].click()
time.sleep(9)
d = browser.find_elements(By.XPATH, "//div[contains(@id, ('driving_status'))]")[0].text
num = ''
for i in d:
    if (ord(i) >= 48 and ord(i) <= 57):
        for j in d[d.index(i):]:
            if j != ' ':
                num = num + j
            else:
                break
        break
num = float(num)
