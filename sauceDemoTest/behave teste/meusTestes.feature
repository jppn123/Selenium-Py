#language: pt

Funcionalidade: Testar a página SauceDemo da SwagLabs

Cenário: Fazer login e entrar na página principal da SauceDemo
    Dado que estou na página de login da SauceDemo
    Quando inserir os dados fornecidos para login, senha e clicar no botão
    Então devo estar na página principal da SauceDemo

Cenário: Estar na página principal da SauceDemo e fazer logout
    Dado que estou na página principal da SauceDemo
    Quando eu clicar no botão menu e clicar na aba logout da navbar
    Então devo estar na página de login da SauceDemo