from selenium import webdriver
from time import sleep
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import chromedriver_binary

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
sleep(5)

contatos = ['Nome contato']
mensagem = 'Vamos na praça? Recado pelo Robo da Drica'

variaveis = {
    'input_pesquisa': '//div[contains(@class,"copyable-text selectable-text")]',
    'input_mensagem': '//div[contains(@class,"copyable-text selectable-text")]'
}


def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath(variaveis['input_pesquisa'])
    sleep(5)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)


def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath(variaveis['input_mensagem'])
    campo_mensagem[1].click()
    sleep(2)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)


for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
