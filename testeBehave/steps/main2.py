from imports import *

BarraDePesquisa = (By.XPATH, '//*[@class="yuRUbf"]/a/h3')
SendKeys = ('python', Keys.ENTER)

@given(u'que já estou na aba de resultados de pesquisa')
def abrirGoogle(context):
    context.driver.get("https://www.google.com/search?q=python")

@when(u'clicar na ancora de redirecionamento do site do python')
def clicarBarraPesquisa(context):
    context.driver.find_element(*BarraDePesquisa).click()

@then(u'deve aparecer o site do python')
def resultados(context):
    spanText = context.driver.title
    assert spanText == "Welcome to Python.org"

