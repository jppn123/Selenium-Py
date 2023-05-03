from biblio import *

driver = Firefox()
driver.get('https://curso-python-selenium.netlify.app/exercicio_04.html')
sleep(3)
ids = ['nome', 'email','senha','telefone','btn']
texts = ['joao', 'jppn@gamer', '12345678', '987654321']

for x in range(len(texts)):
    driver.find_element(By.ID, ids[x]).send_keys(texts[x])
    
driver.find_element(By.ID,ids[-1]).click()

lista_result = list()
sleep(1)
dict_result = driver.find_element(By.XPATH,'/html/body/div/main/textarea').text
dict_result = dict_result.replace("{", '').replace("}", "").replace("\'",'')
dict_result = dict_result.split(", ")
for x in range(len(dict_result)):
    for z in dict_result[x]:	
        if z == ' ':
            ind = dict_result[x].index(z)
            lista_result.append(dict_result[x][ind+1:])

assert lista_result == texts
driver.quit()