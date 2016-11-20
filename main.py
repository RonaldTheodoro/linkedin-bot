from time import sleep 
from selenium import webdriver
from decouple import config


browser = webdriver.Chrome(executable_path='drivers/chromedriver')

url = 'https://www.linkedin.com/uas/login?goback=&trk=hb_signin'

browser.get(url)

email = browser.find_element_by_xpath('//*[@id="session_key-login"]')
password = browser.find_element_by_xpath('//*[@id="session_password-login"]')
sign_in = browser.find_element_by_xpath('//*[@id="btn-primary"]')

email.send_keys(config('EMAIL'))
password.send_keys(config('PASSWORD'))
sign_in.click()

sleep(10)

browser.quit()
