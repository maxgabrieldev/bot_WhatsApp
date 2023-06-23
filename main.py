from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class WhatsappBot: # Classe WhatsappBot
    def __init__(self): # Método construtor
        self.mensagem = 'Testando bot'  # Mensagem que será enviada
        self.grupos = ['outro assunto']     # Grupos que receberão a mensagem
        options = webdriver.ChromeOptions()     # Opções do navegador
        options.add_argument('lang=pt-br')    # Idioma do navegador
        chrome_driver_path = r'./driver/chromedriver.exe'   # Caminho do driver do navegador
        service = Service(chrome_driver_path)   # Serviço do driver
        self.driver = webdriver.Chrome(service=service, options=options)    # Inicialização do driver


    def EnviarMensagens(self):  # Método para enviar mensagens
        self.driver.get('https://web.whatsapp.com/')    # Acessa o site do whatsapp
        time.sleep(10)
        for grupo in self.grupos:   # Para cada grupo na lista de grupos
            grupo_element = self.driver.find_element(By.XPATH, f"//span[@title='{grupo}']")     # Procura o grupo
            time.sleep(3)
            grupo_element.click()
            chat_box = self.driver.find_element(By.CLASS_NAME, '_3Uu1_')    # Procura a caixa de texto
            time.sleep(1)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element(By.XPATH, "//span[@data-icon='send']")  # Procura o botão de enviar
            time.sleep(1)
            botao_enviar.click()    # Clica no botão de enviar
            time.sleep(1)

bot = WhatsappBot()     # Instancia o objeto bot
bot.EnviarMensagens()   # Chama o método para enviar mensagens


