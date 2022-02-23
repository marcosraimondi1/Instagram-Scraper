import time

# Selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

loadingIcons = ["-","\\","|","/","-","\\","|","/","-","\\"] # for console logging

def get(driver, link_number):
    """
    Scraps Followers Data
    - driver: object (selenium webdriver)
    - link_number: number (li number for xpath (2 -> followers; 3 -> following))
    - returns: list (followers)
    """
    followers = []

    try:

        # obtener cantidad de follows
        xpath = f"/html/body/div[1]/section/main/div/header/section/ul/li[{link_number}]/a/div/span"
        cantidad = int(driver.find_element(
            By.XPATH, xpath).get_attribute('innerHTML'))

        printB(f"Cantidad de follows: {cantidad}")

        # abrir pop up requerido
        xpath = f"/html/body/div[1]/section/main/div/header/section/ul/li[{link_number}]/a"

        driver.find_element(By.XPATH, xpath).send_keys(Keys.ENTER)

        time.sleep(5)

        selector = "a.notranslate._0imsa > span._7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll" # selector para los elementos de la lista     
        
        loadingIndex = 0
        items = []

        # scrollear hasta encontrar todos los follows
        while True:

            # conseguir los elementos a traves con el css selector
            items = driver.find_elements(By.CSS_SELECTOR, selector)
            
            loadingIndex += 1 # for loading animation

            if len(items) == len(followers) and len(followers) < cantidad:
                time.sleep(0.1)
                continue # sin cambios

            # guardar los nombres de los usuarios en la lista
            for item in items[len(followers):]:
                try:
                    followers.append(item.get_attribute('innerHTML')) # extract text
                except Exception as ex:
                    print(ex)
                    continue

            printB(f"{len(followers)} / {cantidad} {loadingIcons[loadingIndex%10]}")
            
            if (len(followers) >= cantidad):
                # terminar el ciclo -> todos los datos conseguidos
                break          

            # scrollear para cargar mas elementos
            try:
                driver.execute_script(
                    "document.getElementsByClassName('isgrP')[0].scrollTop = 9999999")
            except Exception:
                break
        
        printB("Scrolling Ended")      

    except NoSuchElementException:
        printB("no such element")
    
    except Exception:
        printB("Something went wrong . . .")

    # Close Pop Up
    xpath = "/html/body/div[6]/div/div/div/div[1]/div/div[2]/button"
    try:
        driver.find_element(By.XPATH, xpath).send_keys(Keys.ENTER)
    except NoSuchElementException:
        # refresh page
        driver.refresh()
        printB("error closing, refreshing page")
        time.sleep(5)

    printB("Scraping ended . . .")

    return followers


def printB(message):
    """
    Decorator for printing
    - message: string
    """
    print("------------------------------------------")
    print(message)
    print("------------------------------------------")
