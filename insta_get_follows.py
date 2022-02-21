import time

# Selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def get_follows(driver, link_number):
    """
    Scraps Followers Data
    - driver: object (selenium webdriver)
    - link_number: number (li number for xpath (2 -> followers; 3 -> following))
    - returns: list (followers)
    """
    followers = []

    try:
        # abrir pop up requerido
        xpath = f"/html/body/div[1]/section/main/div/header/section/ul/li[{link_number}]/a"
        driver.find_element(By.XPATH, xpath).send_keys(Keys.ENTER)

        # scroll div para que rendericen todos los elementos de la lista
        time.sleep(5)

        driver.execute_script(
            "document.getElementsByClassName('isgrP')[0].scrollTop = 150000")

        time.sleep(5)

        # conseguir los elementos a traves con el css selector
        selector = "a.notranslate._0imsa > span._7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll"
        items = driver.find_elements(
            By.CSS_SELECTOR, selector)

        # guardar los nombres de los usuarios en la lista
        for item in items:
            followers.append(item.get_attribute('innerHTML'))

    except NoSuchElementException:
        printB("no such element")

    # Close Pop Up
    xpath = "/html/body/div[6]/div/div/div/div[1]/div/div[2]/button"
    try:
        driver.find_element(By.XPATH, xpath).send_keys(Keys.ENTER)
    except NoSuchElementException:
        printB("error closing")

    return followers


def printB(message):
    """
    Decorator for printing
    - message: string
    """
    print("------------------------------------------")
    print(message)
    print("------------------------------------------")
