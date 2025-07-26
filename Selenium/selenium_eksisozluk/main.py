from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

browser = webdriver.Chrome()

url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="

entryCount = 1
whilecounter = 1
entries = []

while whilecounter <=5:
    randomPage  = random.randint(1,3055) #3055 sayfa var şuan toplama
    newUrl = url + str(randomPage)
    browser.get(newUrl)
    time.sleep(random.uniform(1.5, 3.0))
    elements = browser.find_elements(By.CLASS_NAME, 'content')

    for i in elements:
        entries.append(i.text)
    
    whilecounter +=1

with open ("entries.txt","w",encoding="UTF-8") as file:
    for entry in entries:
        file.write(str(entryCount) + ".\n" + entry + "\n")
        file.write("**********************\n")
        entryCount += 1

browser.close()