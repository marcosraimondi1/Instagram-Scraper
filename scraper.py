from operator import index
from config_driver import config_driver
from insta_login import login
from insta_get_followers import get_followers, printB
from insta_get_following import get_following

# System
from os import environ
import time
from dotenv import load_dotenv

# Pandas
import pandas


def scrap_instagram():
    """
    Scraps Instagram to check followers following status
    """

    insta_user = environ.get("INSTA_USER")
    insta_pass = environ.get("INSTA_PASS")

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
    followers = get_followers(driver)

    time.sleep(2)

    # conseguir lista de seguidos
    following = get_following(driver)

    data = dict()
    data["yo"] = "te sigue"

    for follower in followers:
        if follower in following:
            data[follower] = "te sigue"
        else:
            data[follower] = "no te sigue"

    dataFrame = pandas.DataFrame(data.items())
    dataFrame.columns = ["seguidores", "estado"]

    printB(dataFrame)

    time.sleep(2)


def main():
    load_dotenv()  # load environment variables

    scrap_instagram()


if __name__ == "__main__":
    main()
