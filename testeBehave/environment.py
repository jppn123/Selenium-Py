from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

def before_all(context):
    options = FirefoxOptions()
    options.add_argument('-headless')
    options.add_argument('-window-size=1920,1080')
    options.add_argument('-start-maximized')
    context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    

def before_step(context, step):
    context.driver.implicitly_wait(10)

# def before_scenario(context, scenario):
#     print("aqui você faz alterações antes que um cenário em .features mude")
    
# def before_feature(context, feature):
#     print("aqui você faz alterações antes que uma funcionalidade em .features mude")

def after_all(context):
    context.driver.quit()

# escrever behave no terminal linux para testar 
# no windows deve-se adicionar o arquivo: 
'''
behave.ini 
e colocar dentro do arquivo:

[behave.formatters]
plain.color = behave_plain_color_formatter:PlainColorFormatter

e então no terminal, digitar:

behave -f plain.color 
ou 
python -m behave -f plain.color

'''