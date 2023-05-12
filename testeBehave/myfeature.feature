#language: pt

Funcionalidade: Testes

Cenário: Buscar por python na barra de pesquisa do google
    Dado que entrei na página do google
    Quando clicar na barra de pesquisa
        E digitar "python" e a tecla enter 
    Então deve aparecer os resultados da pesquisa

Cenário: Clicar no site do python
    Dado que já estou na aba de resultados de pesquisa
    Quando clicar na ancora de redirecionamento do site do python
    Então deve aparecer o site do python