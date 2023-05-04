# Entrar na aplicação, preencher login simples, clicar em logar e interagir com o alert.

from biblio import *

driver.get("https://omayo.blogspot.com/")

# element = driver.find_element(By.NAME,'login')
# driver.execute_script("arguments[0].scrollIntoView();", element)
userid = "joao"
senha = "123"

driver.find_element(By.NAME, 'userid').send_keys(userid)
driver.find_element(By.NAME, 'pswrd').send_keys(senha)
driver.find_element(By.XPATH,'//*[@name="login"]/input[@type="button"]').click()

alert = WebDriverWait(driver,10).until(ec.alert_is_present(), 'não achei o alerta')
alert.accept()
name = driver.find_element(By.NAME, 'userid')
password = driver.find_element(By.NAME, 'pswrd')

# se os dados dos inputs não apagarem eles ficarão contidos no atributo value do input
assert name.get_attribute("value") == userid and password.get_attribute("value") == senha, 'não está correto'

# assert name.get_attribute("value") == '' and password.get_attribute("value") == '', 'não está correto'