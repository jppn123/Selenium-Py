from imports import *

class teste():
    def __init__(self, url):
        self.driver = Firefox()
        self.driver.get(url)
    
    def testa_cor(self, xpath: str, hex_cor: str, css_property: str):
        corHeader = Color.from_string(self.driver.find_element(By.XPATH, xpath).value_of_css_property(css_property)).hex
        assert corHeader == hex_cor, f'cor {corHeader} diferente de {hex_cor}'
        print("passou no teste de cor")
    
    def b_tag(self, texto):
        btag = self.driver.find_elements(By.TAG_NAME, 'b')
        assert len(btag) == 1, 'quantidade de palavras em negrito errada'
        assert btag[0].text == texto, f'o texto {texto} não foi encontrado'

    def testa_ancora(self):
        As = []
        AsRepetidos = []
        
        ancoras = self.driver.find_elements(By.XPATH, '//*[@class="col-lg-6"]/a')
        for idLink in ancoras:
            if idLink.get_attribute('href') not in As:
                As.append(idLink.get_attribute('href'))
            else:
                AsRepetidos.append(idLink.get_attribute('href'))

        print(f'a página possui {len(As)} âncoras, onde {len(AsRepetidos)} delas estão repetidos sem necessidade, são elas:\n')
        for Arepetido in AsRepetidos:
            print(Arepetido)
        print()
            

    def itens_repetidos(self):
        # tratamento dos textos repetidos e indicação de quais são eles
        textos = []
        textosRepetidos = []
        texts = self.driver.find_element(By.XPATH, '//*[@class="col-lg-6"]')
        textsEdit = texts.text.split("\n")
        for txt in textsEdit:
            if txt not in textos:
                textos.append(txt)
            else:
                textosRepetidos.append(txt)
    
        print(f'a página possui {len(textosRepetidos)} textos repetidos sem necessidade, são eles:\n')
        for textoRepetido in textosRepetidos:
            print(textoRepetido)
        print()
                
        

    def sair(self):
        self.driver.quit()


t = teste("https://testlink.org")
# t.testa_cor('//*[@class="header"]/h3', '#999999', 'color')
# t.testa_cor('//*[@class="jumbotron"]', '#eeeeee', 'background-color')
# t.b_tag('(1.9.20 - Raijin)')

t.testa_ancora()
# t.itens_repetidos()


# t.sair()


