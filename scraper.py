# System
from os import environ
import time
from dotenv import load_dotenv

# Beautiful Soup
from bs4 import BeautifulSoup

# Pandas
import pandas

# Selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def printB (message):
    """
    Decorator for printing
    - message: string
    """
    print("------------------------------------------")
    print(message)
    print("------------------------------------------")


def login(insta_user, insta_pass, driver):
    """
    Login to Instagram
    - insta_user: string (instagram username)
    - insta_pass: string (instagram password)
    - driver: object (selenium webdriver)
    - returns: boolean (if logged in)
    """
    try:
        # Username
        elemento = driver.find_element(By.NAME, "username")
        elemento.send_keys(insta_user)

        # Password
        elemento = driver.find_element(By.NAME, "password")
        elemento.send_keys(insta_pass)

        # Submit
        elemento = driver.find_element(
            By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")

        elemento.send_keys(Keys.ENTER)

        return True

    except Exception:
        return False


def get_followers(insta_user, driver):
    """
    Scraps Followers Data
    - insta_user: string (instagram username)
    - driver: object (selenium webdriver)
    - returns: void
    """

    actions = ActionChains(driver)

    path = f"https://www.instagram.com/{insta_user}"
    driver.get(path)

    # followers link
    elemento = driver.find_element(
        By.XPATH, "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
    elemento.send_keys(Keys.ENTER)

    # scrap data
    item = 1
    followers = dict()  # dict mapping followers to boolean (if follower is following)

    while True:
        xpath = f"/html/body/div[6]/div/div/div/div[2]/ul/div/li[{item}]/div/div[2]/div[1]/div/div/span/a/span"

        try:
            elemento = driver.find_element(By.XPATH, xpath)

            # get follower username
            follower_user = elemento.get_attribute('innerHTML')
            followers[follower_user] = False  # initialized in false

            # scroll to element to load next li
            actions.move_to_element(elemento).perform()

            print(follower_user)

        except Exception as err:
            
            printB(f"Error: {type(err)} -- {err}")
            break

        item += 1

    printB("scraping ended")


def scrap_instagram():
    """
    Scraps Instagram to check followers following status
    """

    insta_user = environ.get("INSTA_USER")
    insta_pass = environ.get("INSTA_PASS")

    # chrome driver config
    driver = webdriver.Chrome("chromedriver.exe")
    driver.implicitly_wait(10)  # tiempo de espera para ejecutar cada accion

    driver.get("https://instagram.com")

    time.sleep(2)

    logged = login(insta_user, insta_pass, driver)

    if not logged:
        return

    time.sleep(2)

    get_followers(insta_user, driver)

    time.sleep(120)


def main():
    load_dotenv()  # load environment variables

    scrap_instagram()


if __name__ == "__main__":
    main()
