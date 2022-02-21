from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


def login(insta_user, insta_pass, driver):
    """
    Login to Instagram
    - insta_user: string (instagram username)
    - insta_pass: string (instagram password)
    - driver: object (selenium webdriver)
    - returns: void
    """
    try:
        # Completar username
        driver.find_element(By.NAME, "username").send_keys(insta_user)

        # Completar password
        driver.find_element(By.NAME, "password").send_keys(insta_pass)

        # Click en submit
        xpath = "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button"
        driver.find_element(
            By.XPATH, xpath).send_keys(Keys.ENTER)

    except NoSuchElementException:
        return
