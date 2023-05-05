from biblio import *
'''
1. Você deve fazer a automação abrir 5 abas ou janelas de sua escolha;
2. No seu arquivo deve possuir uma função com as seguintes características:
    - input: Uma string
    - output: A url da aba que contém a String passada por parâmetro
'''
driver.get("https://www.youtube.com/watch?v=6ePZqrdgVuw")
driver.switch_to.new_window("tab")
driver.get("https://www.selenium.dev/documentation/webdriver/interactions/alerts/")
driver.switch_to.new_window("tab")
driver.get("https://meet.google.com")
driver.switch_to.new_window("tab")
driver.get("https://music.youtube.com")
driver.switch_to.new_window("tab")
driver.get("https://www.digitalocean.com/community/tutorials/como-criar-um-pull-request-no-github-pt")

def window(string: str) -> str:
    windows = driver.window_handles
    for window in windows:
        driver.switch_to.window(window)
        if string in driver.current_url:
            return f'a palavra "{string}" está contida na url: {driver.current_url}'
    return f'a palavra "{string}" não está contida em nenhuma url'

print(window("digital"))