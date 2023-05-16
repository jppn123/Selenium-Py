from .imports import *

class Base(imp):
    def __init__(self):
        self.options = FirefoxOptions()
        self.options.add_argument('-headless')
        self.options.add_argument('-window-size=1920,1080')
        self.options.add_argument('-start-maximized')
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=self.options)
    
    def find(self, elemento):
        sleep(1)
        return self.driver.find_element(*elemento)
    
    def send(self, elemento, key):
        self.find(elemento).send_keys(*key)

class Actions(Base):
    def entrarPage(self):
        self.driver.get(self.URL)
        
    def login(self, login, senha):
        self.send(self.LOGIN, login)
        self.send(self.SENHA, senha)
        self.find(self.IDBUTTON).click()
    
    def logout(self):
        self.find(self.IDMENU).click()
        self.find(self.LOGOUTBUTTON).click()
    
    # vai ser o after_all do behave
    def quit(self):
        self.driver.quit()