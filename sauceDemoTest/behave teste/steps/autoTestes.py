from behave import *
import sys
sys.path.insert(0,"..")
from main.Classes import *

a = Actions()

@given(u'que estou na página de login da SauceDemo')
def entrarPagina(context):
    a.entrarPage()
    
@when(u'inserir os dados fornecidos para login, senha e clicar no botão')
def fazerLogin(context):
    LOGINKEY = 'standard_user'
    SENHAKEY = 'secret_sauce'
    a.login(LOGINKEY, SENHAKEY)

@then(u'devo estar na página principal da SauceDemo')
def estouNaPagina(context):
    assert a.find((By.XPATH, '//*[@class="title"]')).text == 'Products'



@given(u'que estou na página principal da SauceDemo')
def estouNaPagina(context):
    assert a.find((By.XPATH, '//*[@class="title"]')).text == 'Products'

@when(u'eu clicar no botão menu e clicar na aba logout da navbar')
def fazerLogout(context):
    a.logout()

@then(u'devo estar na página de login da SauceDemo')
def estouNaPagina(context):
    assert a.find((By.XPATH, '//*[@class="login_logo"]')).text == 'Swag Labs'
    a.quit()
    
