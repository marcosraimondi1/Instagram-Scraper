import time

# Selenium
from selenium.webdriver.common.action_chains import ActionChains
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
    actions = ActionChains(driver)
    try:
        # followers link
        xpath = f"/html/body/div[1]/section/main/div/header/section/ul/li[{link_number}]/a"
        driver.find_element(By.XPATH, xpath).send_keys(Keys.ENTER)

        time.sleep(10)

        # scrap data
        # Scroll Down
        i = 1
        while True:
            try:
                xpath = f"/html/body/div[6]/div/div/div/div[2]/ul/div/li[{i}]"
                elemento = driver.find_element(By.XPATH, xpath)
                followers.append(elemento.get_attribute('innerHTML'))
                print(elemento.get_attribute("hidden"))
                # elemento.send_keys(Keys.DOWN)
                actions.move_to_element(elemento).perform()
                i += 1
            except NoSuchElementException:
                break

        items = driver.find_elements(
            By.CSS_SELECTOR, "span._7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll")

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

    return list(set(followers))


def printB(message):
    """
    Decorator for printing
    - message: string
    """
    print("------------------------------------------")
    print(message)
    print("------------------------------------------")
