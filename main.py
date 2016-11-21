from time import sleep 
from selenium import webdriver
from decouple import config


def login_linkedin():
    # User chrome driver
    browser = webdriver.Chrome(executable_path='drivers/chromedriver')

    # Linkedin's url
    url = 'https://www.linkedin.com/uas/login?goback=&trk=hb_signin'

    # Get html
    browser.get(url)

    # Find email input
    email = browser.find_element_by_xpath('//*[@id="session_key-login"]')
    # Find password input
    password = browser.find_element_by_xpath(
        '//*[@id="session_password-login"]')
    # Find login button
    sign_in = browser.find_element_by_xpath('//*[@id="btn-primary"]')

    # Send keys
    email.send_keys(config('EMAIL'))
    password.send_keys(config('PASSWORD'))
    
    # Login
    sign_in.click()

    sleep(10)

    # Close browser
    browser.quit()


if __name__ == '__main__':
    login_linkedin()
    