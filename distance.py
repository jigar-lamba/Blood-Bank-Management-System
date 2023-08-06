import sqlite3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
conn = sqlite3.connect('C:/Users/riyaa/Music/bloodbankmanagement-master/db.sqlite3')
cur = conn.cursor()

last_row = cur.execute('select * from donor_donor').fetchall()[-1]
browser = webdriver.Edge(executable_path = 'C:/Users/riyaa/edgedriver_win64/msedgedriver')
browser.get('https://www.mapdevelopers.com/distance_from_to.php')
browser.find_element(By.XPATH, "//input[contains(@id, 'fromInput-map-control')]").send_keys('Thapar Institute of Engineering and Technology, Patiala')
browser.find_element(By.XPATH, "//input[contains(@id, 'toInput-map-control')]").send_keys(last_row[3])
x = browser.find_elements(By.XPATH, "//button[contains(@id, ('calculate-distance-map-control'))]")[0].click()
time.sleep(9)
d = browser.find_elements(By.XPATH, "//div[contains(@id, ('driving_status'))]")[0].text
num = ''
for i in d:
    if (ord(i) >= 48 and ord(i) <= 57):
        print(d.index(i))
        for j in d[d.index(i):]:
            if j != ' ':
                num = num + j
            else:
                break
        break
num = float(num)
cur.execute('UPDATE donor_donor SET dist ='+str(num)+' WHERE id ='+str(last_row[0]))
conn.commit()
last_row = cur.execute('select * from donor_donor').fetchall()[-1]
print(last_row)
conn.close()
