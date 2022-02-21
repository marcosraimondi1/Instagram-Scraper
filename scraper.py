# System
import sys
from os import environ
import time
from dotenv import load_dotenv

# Custom Modules
from config_driver import config_driver
from insta_login import login
from insta_get_follows import get_follows, printB
from process_data import process_data


def scrap_instagram():
    """
    Scraps Instagram to check followers following status
    """

    insta_user = environ.get("INSTA_USER")
    insta_pass = environ.get("INSTA_PASS")

    if not insta_user:
        insta_user = sys.argv[1]
        insta_pass = sys.argv[2]

    # chrome driver config
    driver = config_driver()

    driver.get("https://instagram.com")

    # login
    login(insta_user, insta_pass, driver)

    time.sleep(2)

    # ir al perfil del usuario
    path = f"https://www.instagram.com/{insta_user}"
    driver.get(path)

    time.sleep(2)

    # conseguir lista de seguidores
    followers = get_follows(driver, 2)

    time.sleep(2)

    # conseguir lista de seguidos
    followings = get_follows(driver, 3)

    process_data(followers, followings)


def main():

    if len(sys.argv) != 3:
        printB("Usage: py scraper.py <username> <password>")
        return

    load_dotenv()  # load environment variables

    scrap_instagram()


if __name__ == "__main__":
    main()
