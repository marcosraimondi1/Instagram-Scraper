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
    Scraps Instagram to check followers/following status
    """

    insta_user = environ.get("INSTA_USER")
    insta_pass = environ.get("INSTA_PASS")
    extra_username = False
    if not insta_user:
        # si no hay variables del .env (para dev), usamos los datos ingresados (para prod)
        insta_user = sys.argv[1]
        insta_pass = sys.argv[2]
        if len(sys.argv) > 3:
            extra_username = sys.argv[3]

    # chrome driver config
    driver = config_driver()
    
    driver.maximize_window()

    driver.get("https://instagram.com") # navegamos a la pagina

    login(insta_user, insta_pass, driver) # nos logueamos

    time.sleep(2)

    # ir al perfil del usuario
    if extra_username:
        path = f"https://www.instagram.com/{extra_username}/"
        driver.get(path)
    else:
        path = f"https://www.instagram.com/{insta_user}/"
        driver.get(path)

    time.sleep(2)

    followers = get_follows(driver, 2) # conseguimos lista de seguidores

    time.sleep(2)

    followings = get_follows(driver, 3) # conseguir lista de seguidos

    process_data(followers, followings) # procesamos los datos


def main():

    if len(sys.argv) < 3:
        # se ingresan usuario y contraseña de instagram al ejecutar
        printB("Usage: py scraper.py <username> <password> <usernames_to_scrap>")
        return
    elif len(sys.argv) >3:
        printB(f"Starting web scraping for: {sys.argv[2:]}")
    else:
        printB(f"Starting web scraping for: {sys.argv[1]}")

    load_dotenv()  # load environment variables

    scrap_instagram()


if __name__ == "__main__":
    main()
