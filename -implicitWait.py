from biblio import *

driver = Firefox()

driver.get("https://selenium.dunossauro.live/aula_09_a.html")
driver.implicitly_wait(10)
driver.find_element(By.ID, 'request').click()
concluido = driver.find_element(By.ID,'finished').text
assert concluido == 'Carregamento concluído', 'não encontrei o texto'

driver.quit()