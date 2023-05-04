# Entrar na aplicação, interagir com o prompt, escrever algo e clicar em "OK"

from biblio import *

driver.get("https://omayo.blogspot.com")

driver.find_element('id', 'prompt').click()

alert = WebDriverWait(driver,10).until(ec.alert_is_present())
alert.send_keys("joao")
alert.accept()