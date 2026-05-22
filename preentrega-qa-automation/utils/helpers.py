
# set up de selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# funcion para el set-up del driver
def setup_driver():
    chrome_options = Options()
    # opciones 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--guest")
    
    service = Service()
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    return driver

#funcion que inicia el driver
def test_login_saucedemo():
    driver = setup_driver()

#inicia el driver
if __name__ == "__main__":
    test_login_saucedemo()