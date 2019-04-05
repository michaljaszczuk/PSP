from selenium.webdriver.common.by import By

'''
Page Object of https://www.phptravels.net/public/expedia/
with variables(locators)
and methods(actions defined by tester, which user can take on this particular page)
'''

# URL
APP = 'https://www.phptravels.net/public/expedia/'

# Locators
INPUT_SEARCH = 'q'


def open_url(driver):
    driver.get('https://google.pl')


def search_query(driver):
    search_query_box = driver.find_element(By.NAME, INPUT_SEARCH)
    search_query_box.click()
    search_query_box.send_keys('Paris')
    search_query_box.submit()
