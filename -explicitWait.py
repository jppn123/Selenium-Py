from biblio import *

driver = Firefox()
driver.get("https://selenium.dunossauro.live/aula_09_a.html")
wait = WebDriverWait(driver, 10)
# como o unico parametro da função dentro do .until() deve ser o webDriver, então pode-se usar a função lambda para enviar ao
# until o elemento presente no webDriver, já que o .until() consegue conter o valor do retorno da função que está dentro dele

clicar_no_botao = wait.until(
    lambda WebDriver: 
        WebDriver.find_element(By.ID, 'request'), 
    'não achei o botão então não vou clicar!'
).click()
# button.click()

resgatar_a_mensagem = wait.until(
    lambda WebDriver: 
        WebDriver.find_element(By.ID,'finished'), 
    'não encontrei a mensagem então não vou te devolver nenhum texto!'
).text
# message = message.text

assert resgatar_a_mensagem == 'Carregamento concluído', 'não encontrei o texto'
driver.quit()