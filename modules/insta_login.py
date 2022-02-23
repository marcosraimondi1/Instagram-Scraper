import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from modules.insta_get_follows import printB


def login(insta_user, insta_pass, driver):
    """
    Login to Instagram
    - insta_user: string (instagram username)
    - insta_pass: string (instagram password)
    - driver: object (selenium webdriver)
    - returns: void
    """
    try:
        tries = 0
        while tries < 10:
            # navegamos a la pagina
            driver.get("https://instagram.com") 

            time.sleep(3)
            
            # Completar username
            driver.find_element(By.NAME, "username").send_keys(insta_user)

            # Completar password y enter
            driver.find_element(By.NAME, "password").send_keys(insta_pass, Keys.ENTER)

            time.sleep(1.5)

            # Ver si hay mensaje de error
            try:
                error = driver.find_element(By.ID, "slfErrorAlert")
                printB(f"Error: {error.get_attribute('innerHTML')} \n trying again in 10 seconds")
                time.sleep(10)
                tries += 1
                login(insta_user, insta_pass, driver)

            except NoSuchElementException:
                print("Login successful")
                return
    except Exception as ex:
        raise Exception(f"Failed to login: {ex}")
