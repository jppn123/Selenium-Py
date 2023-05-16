from .imports import *

class Base(imp):
    def __init__(self): 
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    
    def find(self, elemento):
        sleep(1)
        return self.driver.find_element(*elemento)
    
    def send(self, elemento, key):
        self.find(elemento).send_keys(*key)

class Login(Base):
    def enviarUser(self, username):
        self.send(self.LOGIN, username)
        
    def enviarSenha(self, senha):
        self.send(self.SENHA, senha)
        
    def enviarDados(self):
        self.find(self.IDBUTTON).click()
        
class Logout(Base):
    def clicarMenu(self):
        self.find(self.IDMENU).click()
    
    def clicarLogout(self):
        self.find(self.LOGOUTBUTTON).click()
        
class Actions(Login, Logout):
    def entrarPage(self):
        self.driver.get(self.URL)
    
    def quit(self):
        self.driver.quit()