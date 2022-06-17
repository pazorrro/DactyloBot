#import des bibliothèqye
from selenium import webdriver
import time

#ouverture du navigateur
driver = webdriver.Chrome('chromedriver')

#va sur la page de test de dyctalographie
driver.get('https://10fastfingers.com/typing-test/french')
time.sleep(5)


#clique sur le bouton des cookies pour commencer
driver.find_element_by_xpath(".//button[@class='CybotCookiebotDialogBodyButton']").click()
time.sleep(3)

#bat de reccord du monde
for i in range(150):
    url1=".//span[@wordnr='"
    url2=str(i)
    url3="']"
    url=url1+url2+url3
    texte = driver.find_element_by_xpath(url).text
    driver.find_element_by_xpath(".//input[@class='form-control']").send_keys(texte)
    driver.find_element_by_xpath(".//input[@class='form-control']").send_keys(" ")
