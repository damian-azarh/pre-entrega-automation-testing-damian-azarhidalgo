# pre-entrega-automation-testing-damian-azarhidalgo
Pre entrega Curso QA Automation Testing 
Este proyecto implementa una automatización de pruebas para el sitio SauceDemo, utilizando Selenium WebDriver y Python.

Propósito del Proyecto

El objetivo es automatizar los siguientes flujos en la aplicación SauceDemo:
Login con credenciales válidas e inválidas
Verificación del catálogo de productos
Interacción con el carrito de compras (añadir productos y verificar su contenido)
Cierre de sesión

Tecnologías Utilizadas
Python: Lenguaje de programación principal
Pytest: Framework de testing para estructurar y ejecutar pruebas
Selenium WebDriver: Para la automatización de la interfaz web
Git/GitHub: Para control de versiones y compartir el código

Estructura del Proyecto
pre-entrega-qa-automation/
/utils├── helpers.py # Funciones auxiliares reutilizables 
/tests├── test_saucedemo.py # Casos de prueba automatizados 

Funcionalidades Implementadas

Automatización de Login Caso de éxito con credenciales válidas
Caso de fallo con credenciales inválidas

Verificación del Catálogo Comprobación del título de la página
Verificación de presencia de productos
Validación de elementos de la interfaz (menú, filtros, etc.)
Interacción con el Carrito Añadir producto al carrito
Verificar que el contador se incremente
Navegar al carrito
Comprobar que el producto añadido aparezca correctamente
Cierre de Sesión Verificar que el usuario pueda cerrar sesión correctamente

Alumno: Azar Hidalgo, Damian

📝 Notas Este proyecto fue desarrollado como pre-entrega para el curso de Automatización de Testing. Todas las pruebas están diseñadas para funcionar con el sitio web SauceDemo en su versión actual.
