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
        # <span dir="auto" title="outro assunto" class="_3ko75 _5h6Y_ _3Whw5">outro assunto</span>
        # <div tabindex="-1" class="_3uMse">
        # <span data-testid="send" data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(5)
            botao_enviar.click()
            time.sleep(5)
            
bot = WhatsappBot()
bot.EnviarMensagens()