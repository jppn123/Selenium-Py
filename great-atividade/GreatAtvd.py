from imports import *

class teste(importants):
    def __init__(self, url):
        self.driver = Firefox()
        self.driver.get(url)
    
    def testa_cor(self):
        corHeader = Color.from_string(self.driver.find_element(By.XPATH, self.XPATH_HEADER).value_of_css_property("color")).hex
        assert corHeader == self.COR_HEADER, f'cor {corHeader} diferente de {self.COR_HEADER}'
        print("passou no teste de cor")
    
t = teste("https://testlink.org")
t.testa_cor()