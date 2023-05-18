from utils.imports import *
from utils.locators import gitHubLocators

class githubPage(gitHubLocators):
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def entrar(self):
        self.driver.get(self.URL)

    def find(self, locator):
        return self.driver.find_element(*locator)
    
class testeCase(githubPage):
    def clicarRepo(self):
        self.find(self.REPOLOC).click()
    

