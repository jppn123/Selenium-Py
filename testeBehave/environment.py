from selenium.webdriver import Firefox

def before_all(context):
    context.driver = Firefox()

def before_step(context, step):
    context.driver.implicitly_wait(10)

# def before_scenario(context, scenario):
#     print("aqui você faz alterações antes que um cenário em .features mude")
    
# def before_feature(context, feature):
#     print("aqui você faz alterações antes que uma funcionalidade em .features mude")

def after_all(context):
    context.driver.quit()

# escrever behave no terminal para testar 