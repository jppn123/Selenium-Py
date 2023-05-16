from behave import *
import sys
sys.path.insert(0,"..")
from main.Classes import *

a = Actions()
LOGINKEY = 'standard_user'
SENHAKEY = 'secret_sauce'

@given(u'que estou na página de login da SauceDemo')
def entrarPagina(context):
    a.entrarPage()
    
@when(u'inserir os dados fornecidos para login')
def dadosUser(context):
    a.enviarUser(LOGINKEY)

@when(u'inserir os dados fornecidos para senha')
def dadosSenha(context):
    a.enviarSenha(SENHAKEY)

@when(u'clicar no botão enviar')
def botaoEnviarDados(context):
    a.enviarDados()

@then(u'devo estar na página principal da SauceDemo')
@given(u'que estou na página principal da SauceDemo')
def estouNaPagina(context):
    assert a.find((By.XPATH, '//*[@class="title"]')).text == 'Products'

@when(u'eu clicar no botão menu')
def fazerLogout1(context):
    a.clicarMenu()

@when(u'eu clicar na aba logout da navbar')
def fazerLogout2(context):
    a.clicarLogout()

@then(u'devo estar na página de login da SauceDemo')
def estouNaPagina(context):
    assert a.find((By.XPATH, '//*[@class="login_logo"]')).text == 'Swag Labs'
    a.quit()
    
