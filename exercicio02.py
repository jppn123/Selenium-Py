'''
crie um programa em selenium que
    -jogue o jogo
    -pare o script quando você ganhar
'''
from biblio import *
        
driver = Firefox()
driver.get('https://curso-python-selenium.netlify.app/exercicio_02.html')
sleep(2)

control = True
while control:
    driver.find_element(By.TAG_NAME, 'a').click()
    lista = driver.find_elements(By.TAG_NAME,'p')
    for i in range(2, len(lista)):
        if len(lista[i].text) > 2:
            control = False
    
sleep(2)     
driver.quit()
print('o script foi parado')
