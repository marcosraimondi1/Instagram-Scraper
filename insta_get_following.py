# Beautiful Soup
from bs4 import BeautifulSoup

# Selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def get_following(driver):
    """
    Scraps Following Data
    - driver: object (selenium webdriver)
    - returns: dictionary (mapping of followers to false)
    """
    try:
        # following link
        xpath = "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a"
        driver.find_element(By.XPATH, xpath).send_keys(Keys.ENTER)

        # scrap data

        # TODO

        printB("scraping ended")

    except NoSuchElementException:
        printB("no such element")
        return


def printB(message):
    """
    Decorator for printing
    - message: string
    """
    print("------------------------------------------")
    print(message)
    print("------------------------------------------")
