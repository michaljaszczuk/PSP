from selenium.webdriver.common.by import By


def check_if_results_are_from_wiki(driver):
    if "pl.wikipedia.org" in driver.page_source:
        d = driver.find_element_by_name('q')
        d.click()
        d.clear()
        d.send_keys("Warsaw")
        d.submit()
