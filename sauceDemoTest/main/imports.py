from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import FirefoxOptions

class imp:
    URL = 'https://www.saucedemo.com'
    LOGIN = (By.ID, 'user-name')
    SENHA = (By.ID, 'password')
    IDBUTTON = (By.ID, 'login-button')
    IDMENU = (By.ID, 'react-burger-menu-btn')
    LOGOUTBUTTON = (By.ID, 'logout_sidebar_link')