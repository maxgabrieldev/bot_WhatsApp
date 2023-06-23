from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = 'Testando bot'
        self.grupos = ['outro assunto']
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        chrome_driver_path = r'./driver/chromedriver.exe'
        service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=service, options=options)


    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(10)
        for grupo in self.grupos:
            grupo_element = self.driver.find_element(By.XPATH, f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo_element.click()
            chat_box = self.driver.find_element(By.CLASS_NAME, '_3Uu1_')
            time.sleep(1)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element(By.XPATH, "//span[@data-icon='send']")
            time.sleep(1)
            botao_enviar.click()
            time.sleep(1)

bot = WhatsappBot()
bot.EnviarMensagens()
bot.EnviarMensagens()
bot.EnviarMensagens()

