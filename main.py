from time import sleep
from selenium import webdriver
from decouple import config


# User chrome driver
browser = webdriver.Chrome(executable_path='drivers/chromedriver')

# Linkedin's url
url = 'https://www.linkedin.com/uas/login?goback=&trk=hb_signin'

# Get html
browser.get(url)


def login_linkedin():
    """Login linkedin"""
    # Find email input
    browser.find_element_by_xpath(
        '//*[@id="session_key-login"]').send_keys(config('EMAIL'))
    # Find password input
    browser.find_element_by_xpath(
        '//*[@id="session_password-login"]').send_keys(config('PASSWORD'))
    # Find login button
    browser.find_element_by_xpath('//*[@id="btn-primary"]').click()

    sleep(2)


def search_linkedin(search):
    """Search in linkedin"""
    # Find search box
    browser.find_element_by_xpath(
        '//*[@id="main-search-box"]').send_keys(search)
    # Find search button
    browser.find_element_by_xpath(
        '//*[@id="global-search"]/fieldset/button').click()
    # Send data and click


def close_browser():
    # Close browser
    browser.quit()


if __name__ == '__main__':
    login_linkedin()
    search_linkedin('python')

    browser.find_element_by_xpath(
        '//*[@id="search-types"]/div/ul/li[2]/a').click()
    browser.find_element_by_xpath(
        '//*[@id="facet-N"]/fieldset/div/ol/li[3]/div/label/bdi').click()

    sleep(3)

    for a in browser.find_elements_by_class_name('primary-action-button'):
        a.click()
        input('avancar')

    close_browser()
