from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def config():
    """
    Configures driver
    - returns: object (driver)
    """
    try:

        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        driver.implicitly_wait(10)  # tiempo de espera para ejecutar cada accion
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        driver.maximize_window()
        return driver

    except Exception as ex:
        print(ex)
        return False