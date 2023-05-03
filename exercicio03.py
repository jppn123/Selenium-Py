from biblio import *
        
driver = Firefox()
driver.get('https://curso-python-selenium.netlify.app/exercicio_03.html')
sleep(5)
driver.find_element(By.XPATH,'//*[@id="main"]//a').click()
sleep(1)
main = driver.find_element(By.ID,'main')
a = main.find_elements(By.TAG_NAME, 'a')

for x in range(len(a)): 
    if driver.title == "page_1.html":
        if a[x].get_attribute('attr') == "errado":
            a[x].click()
    else:
        for x  in range(2):
            sleep(5)
            driver.find_element(By.XPATH,'//*[@id="main"]//a').click()  
             
if driver.title == "page_4.html":
    driver.refresh()
# driver.quit()