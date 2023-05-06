from GreatAtvdClasses import AssertTest, GitHubTest

# caso de teste dos asserts
teste1 = AssertTest()
teste1.testa_cor('//*[@class="header"]/h3', '#999999', 'color')
teste1.testa_cor('//*[@class="jumbotron"]', '#eeeeee', 'background-color')
teste1.testa_b_tag()
teste1.testa_url()
teste1.testa_iframe()
teste1.testa_titulo()
teste1.textos_repetidos()
teste1.sair()

# caso de teste do github
teste2 = GitHubTest()
teste2.gitHubTeste("gitignore")
teste2.sair()
