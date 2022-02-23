import time

# Selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

loadingIcons = ["-","\\","|","/","-","\\","|","/","-","\\"] # for console logging

def get(driver, target):
    """
    Scraps Followers Data
    - driver: object (selenium webdriver)
    - link_number: number (li number for xpath (2 -> followers; 3 -> following))
    - returns: list (followers)
    """
    followers = []
    link_number = 2
    if target == "following":
        link_number = 3
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
        ti = time.time()
        
        # scrollear hasta encontrar todos los follows
        while (time.time() - ti) < 15:
            
            # loading animation
            loadingIndex += 1 
            printB(f"{len(followers)} / {cantidad} {loadingIcons[loadingIndex%10]}")

            # conseguir los elementos a traves con el css selector
            items = driver.find_elements(By.CSS_SELECTOR, selector)

            if len(items) == len(followers) and len(followers) < cantidad:
                # sin cambios
                time.sleep(0.2)
                continue
            
            ti = time.time()
            
            # guardar los nombres de los usuarios en la lista
            for item in items[len(followers):]:
                try:
                    followers.append(item.get_attribute('innerHTML')) # extract text
                except Exception as ex:
                    print(ex)
                    continue

            
            
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
    
    except Exception as ex:
        print(ex)
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

    if len(followers) == 0:
        raise Exception(f"Error: {target} list empty")

    return followers


def printB(message):
    """
    Decorator for printing
    - message: string
    """
    print("------------------------------------------")
    print(message)
    print("------------------------------------------")
