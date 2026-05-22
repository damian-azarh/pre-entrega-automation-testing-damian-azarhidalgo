from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

from utils.helpers import setup_driver;()

# setup e inicio del driver de Chrome

def test_login_saucedemo():
    driver = setup_driver()
    
    try:
        # se abre la página de login o inicio de sesion
        driver.get("https://www.saucedemo.com/")
        
        # se espera a que cargue el formulario
        username_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        
        # se ingresan las credenciales
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        
        # se clickea el login
        driver.find_element(By.ID, "login-button").click()
        
        # verificamos que estamos logueados con la página de productos
        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
        print("El login fue exitoso")

        # se verifica el titulo de la pagina de productos
        header_title = driver.find_element(
        By.CSS_SELECTOR, "div.header_secondary_container .title"
        ).text
        assert header_title == "Products", f"Título inesperado: {header_title}"

        # se añade un producto al carrito
        driver.find_element(By.XPATH, "//button[contains(@data-test, 'add-to-cart')]").click()
        
        # se espera a que el badge del producto aparezca en el carrito
        badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        
        # verificamos que el contador del carrito marque 1
        assert badge.text == "1", f"El contador del carrito debe mostar 1, pero muestra {badge.text}"
        print("El producto fue añadido al carrito")
    
        # se hace click en el carrito para verificar que el producto fue añadido
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        cart_item = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "cart_item"))
        )
        print("El producto es visible en el carrito")
        # cerrar sesion
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        ).click()
        
        # se verificas que estemos en la pagina de login
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "login-button"))
        )
        print("Se cerro la sesion exitosamente")
        
        print("Las pruebas fueron completadas con exito")
        return True
    
    except Exception as e:
        print(f"❌ Error durante la prueba: {e}")
        return False
    finally:
        # se cierra el navegador
        print("Se cerrara el navegador")
        driver.quit()

if __name__ == "__main__":
    test_login_saucedemo()