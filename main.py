from time import sleep
from selenium import webdriver
from decouple import config


# User chrome driver
browser = webdriver.Chrome(executable_path='drivers/chromedriver')

# Get html
browser.get('https://www.linkedin.com/uas/login?goback=&trk=hb_signin')


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


def find_element(element):
    """Find just one element"""
    return browser.find_element_by_xpath(element)


def close_browser():
    # Close browser
    browser.quit()


if __name__ == '__main__':
    login_linkedin()
    search_linkedin('python')

    find_element('//*[@id="search-types"]/div/ul/li[2]/a').click()

    find_element(
        '//*[@id="facet-N"]/fieldset/div/ol/li[3]/div/label/bdi').click()

    sleep(2)

    page_num = find_element('//*[@id="results_count"]/div/p/strong[1]')
    page_num = page_num.get_attribute('textContent').replace(',', '')
    page_num = int(page_num) // 10

    url = browser.current_url

    for page in range(1, page_num + 1):
        new_url = url + '&page_num={0}'.format(page)
        browser.get(new_url)

        print('Page number: {}'.format(page))

        for a in browser.find_elements_by_class_name('primary-action-button'):
            print(a)

    close_browser()
