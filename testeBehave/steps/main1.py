from imports import *

BarraDePesquisa = (By.NAME, 'q')
SendKeys = ('python', Keys.ENTER)

@given(u'que entrei na página do google')
def abrirGoogle(context):
    context.driver.get("https://www.google.com/")

@when(u'clicar na barra de pesquisa')
def clicarBarraPesquisa(context):
    context.driver.find_element(*BarraDePesquisa).click()

@when(u'digitar "python" e a tecla enter')
def digitarBarraPesquisa(context):
    context.driver.find_element(*BarraDePesquisa).send_keys(*SendKeys)

@then(u'deve aparecer os resultados da pesquisa')
def resultados(context):
    spanText = context.driver.find_element(By.XPATH, '//*[@data-attrid = "title"]//span').text
    assert spanText == "Python"