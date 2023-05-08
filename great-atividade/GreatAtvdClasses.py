from imports import *

class AssertTest(Imp):
    def __init__(self):
        # deixar o código mais rapido pois o firefox não fica visível, apenas os testes rodam
        # self.options = FirefoxOptions()
        # self.options.add_argument('-headless')
        # self.options.add_argument('-window-size=1920,1080')
        # self.options.add_argument('-start-maximized')
        # self.driver = Firefox(options=self.options)
        self.driver = Firefox()
        self.driver.get(self.URL)
    
    def testa_cor(self, xpath: str, hex_cor: str, css_property: str):
        corDetectada = Color.from_string(self.driver.find_element(By.XPATH, xpath).value_of_css_property(css_property)).hex
        assert corDetectada == hex_cor, f'cor {corDetectada} diferente de {hex_cor}'
        print('Passou no teste de cor')
        
    def testa_b_tag(self):
        btag = self.driver.find_elements(By.TAG_NAME, 'b')
        assert len(btag) == 1, 'quantidade de palavras em negrito errada'
        assert btag[0].text == self.BTAGTEXT, f'o texto {self.BTAGTEXT} não foi encontrado'
        print('Passou no teste de b_tag')

    def textos_repetidos(self):
        # tratamento dos textos repetidos e indicação de quais são eles
        textos = []
        textosRepetidos = []
        texts = self.driver.find_element(By.XPATH, self.XPATHROWMARKETING)
        textsEdit = texts.text.split("\n")
        for txt in textsEdit:
            if txt not in textos:
                textos.append(txt)
            else:
                textosRepetidos.append(txt)
    
        print(f'a página possui {len(textosRepetidos)} textos repetidos sem necessidade, são eles:\n')
        for textoRepetido in textosRepetidos:
            assert textoRepetido in textos, 'o texto na verdade não está repetido'
            print(textoRepetido)
        print()
    
    def testa_url(self):
        assert self.driver.current_url == self.URL, f'essa não é a url, na verdade é essa {self.driver.current_url}'
        print('Passou no teste de url')
    
    def testa_titulo(self):
        assert self.driver.title == self.TITLE, f'esse não é o título, na verdade é esse {self.driver.title}'
        print('Passou no teste de titulo')
    
    def testa_iframe(self):
        iframe = self.driver.find_element(By.XPATH, self.XPATHIFRAME)
        self.driver.switch_to.frame(iframe)
        content = self.driver.find_element(By.XPATH, '//body').text
        assert content == self.IFRAMECONTENT, f'{content} diferente de {self.IFRAMECONTENT}'
        self.driver.switch_to.default_content()
        print("passou no teste do iframe")
        
    def sair(self):
        self.driver.quit()


class GitHubTest(AssertTest):
    def gitHubTeste(self, inputKey):
        linkGitHub = self.driver.find_element(By.XPATH, self.XPATHGITHUBANCHOR)
        link = linkGitHub.get_attribute("href")
        linkGitHub.click()
        assert self.driver.current_url == link, f'essa não é a url, na verdade é essa {self.driver.current_url}'
        assert self.driver.title == self.GITHUBANCHORTITLE, f'esse não é o título, na verdade é esse {self.driver.title}'
        print('Passou no teste de estar na página do github')
        self.gitHubPesquisaTeste(inputKey)
        
    def gitHubPesquisaTeste(self, inputKey):
        self.driver.find_element(By.XPATH, self.BEFOREXPATHINPUTGITHUB).send_keys(inputKey, Keys.ENTER)
        input = self.driver.find_element(By.XPATH, self.AFTERXPATHINPUTGITHUB).get_attribute("value")
        assert input == inputKey, f'{input} não é igual a {inputKey}'
        totalPesquisa = 0

        for x in range(len(self.LISTAXPATHSGITHUT)):
            sleep(0.5)
            nResultados = self.driver.find_element(By.XPATH, self.LISTAXPATHSGITHUT[x]).text	
            totalPesquisa += int(nResultados)
            
        print(f'\nA pesquisa "{inputKey}" possui {totalPesquisa} resultados\n')
        
        