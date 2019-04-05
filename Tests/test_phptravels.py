from POM.HomePage import open_url, search_query
from POM.Listing import check_if_results_are_from_wiki


def test_open_url(driver):
    open_url(driver)


def test_search_query(driver):
    search_query(driver)


def test_check_if_results_are_from_wiki(driver):
    check_if_results_are_from_wiki(driver)


def test_teardown(driver):
    driver.close()
    driver.quit()
