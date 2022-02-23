# System
import sys
from os import environ
import time
from dotenv import load_dotenv

# Custom Modules
from modules import config_driver, insta_login, insta_get_follows, process_data

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
    driver = config_driver.config()

    if not driver:
        print("Driver error: failed to start browser")
        return

    
    try:
        insta_login.login(insta_user, insta_pass, driver) # nos logueamos

        time.sleep(2)
        
        # ir al perfil del usuario
        path = ""
        if extra_username:
            path = f"https://www.instagram.com/{extra_username}/"
        else:
            path = f"https://www.instagram.com/{insta_user}/"

        while driver.current_url != path:
            print(f"redirecting to {path}")
            driver.get(path)
            time.sleep(2)
            
    except Exception as ex:
        print(ex)
        return

    try:

        followers = insta_get_follows.get(driver, "followers") # conseguimos lista de seguidores

        time.sleep(2)

        followings = insta_get_follows.get(driver, "following") # conseguir lista de seguidos
        
        process_data.process(followers, followings) # procesamos los datos

    except Exception as ex:
        print(ex)



def main():

    if len(sys.argv) < 3:
        # se ingresan usuario y contraseña de instagram al ejecutar
        insta_get_follows.printB("Usage: py scraper.py <username> <password> <usernames_to_scrap>")
        return
    elif len(sys.argv) >3:
        insta_get_follows.printB(f"Starting web scraping for: {sys.argv[3]}")
    else:
        insta_get_follows.printB(f"Starting web scraping for: {sys.argv[1]}")

    load_dotenv()  # load environment variables

    scrap_instagram()


if __name__ == "__main__":
    main()
