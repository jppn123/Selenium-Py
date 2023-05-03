'''
gere um dicionário, onde a chave é a tag h1
    -o valor deve ser um novo dicionario
    -cada chave do valor deverá ser o valor de 'atributo'
    -cada valor deve ser o texto contido no elemento
'''
from biblio import *

driver = Firefox()
driver.get('https://curso-python-selenium.netlify.app/exercicio_01.html')
sleep(2)

dici = dict()
dici['h1'] = dict()

ps = driver.find_elements(By.TAG_NAME, 'p')

for x in range(len(ps)):
    dici['h1'][ps[x].get_attribute('atributo')] = ps[x].text
driver.quit()

print(dici)