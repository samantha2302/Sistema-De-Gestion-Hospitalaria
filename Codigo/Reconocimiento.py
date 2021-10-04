# Librerías
import json
import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class Reconocimiento:
    def __init__(self):
        self.driver=None
        self.html = None
        pass

    def Configuracion(self):
        # Opciones de navegación
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-extensions')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.add_argument('--allow-running-insecure-content')
        self.driver = webdriver.Chrome('C:/chromedriver.exe',chrome_options=chrome_options)
        self.driver.set_window_position(2000, 0)
        self.driver.maximize_window()
        time.sleep(1)

    def Iniciar(self):
        # Inicializamos el navegador
        self.driver.get('https://azure.microsoft.com/es-es/services/cognitive-services/face/#demo')
        self.driver.switch_to.default_content()
        self.driver.switch_to.parent_frame()
        self.driver.implicitly_wait(10)
        self.html = WebDriverWait(self.driver, 15).until(
                        EC.presence_of_element_located((By.XPATH, 'html'))
                    )

    def ComprobaciónFacial(self,rutaImagen1,rutaImagen2):
        button = self.html.find_element_by_xpath('//*[@id="demo"]/div[3]/div/div/ol/li[2]/button')
        button.click()
        self.driver.implicitly_wait(10)
        confianzaInicial = self.html.find_element_by_xpath(
            '//*[@id="face-verification-demo-results"]/div[2]/p/span').text.split(" ")[3][:-1]

        botonImagen1 = self.html.find_element_by_xpath("//*[@id='face-verification-demo-results']/div[1]/div[2]/div[2]/ul/li[3]/input")
        botonImagen1.send_keys(os.getcwd() + "/" + rutaImagen1)
        self.driver.implicitly_wait(10)
        time.sleep(5)

        botonImagen2 = self.html.find_element_by_xpath("//*[@id='face-verification-demo-results']/div[1]/div[1]/div[2]/ul/li[3]/input")
        botonImagen2.send_keys(os.getcwd() + "/" + rutaImagen2)
        self.driver.implicitly_wait(10)
        time.sleep(5)

        confianzaFinal=confianzaInicial
        print("Esperando respuesta .........")
        contador=0
        time.sleep(5)
        while confianzaInicial==confianzaFinal:
            if contador==10:
                confianzaFinal=0
                break
            confianzaFinal=self.html.find_element_by_xpath('//*[@id="face-verification-demo-results"]/div[2]/p/span').text.split(" ")[3][:-1]
            time.sleep(1)
            contador=contador+1

        return confianzaFinal

    def ReconocerRostro(self,rutaImagen):
        select= self.html.find_element_by_id('DetectionModel')
        for option in select.find_elements_by_tag_name('option'):
            if option.text == 'detection_01':
                option.click()
                time.sleep(2)
                faceid=self.html.find_element_by_xpath(
                    '//*[@id="face-detection-results"]/div/div[2]/div[1]/div/pre/code/span[10]/span[8]').text
                faceidNew=faceid
                break
        try:
            select.find_element_by_xpath("/option[text()='detection_01']")
        except:
            pass
        botonImagen=self.html.find_element_by_xpath("//input[@type='file']")
        botonImagen.send_keys(os.getcwd()+"/"+rutaImagen)
        self.driver.implicitly_wait(10)
        print("Esperando respuesta .........")
        while faceid==faceidNew:
            try:
                faceidNew = self.html.find_element_by_xpath(
                    '//*[@id="face-detection-results"]/div/div[2]/div[1]/div/pre/code/span[10]/span[8]').text
                time.sleep(1)
            except:
                pass
        texto=self.html.find_element_by_xpath('//*[@id="face-detection-results"]/div/div[2]/div[1]/div/pre/code/span[10]')
        texto = texto.text
        jsonObject = json.loads(texto)
        return jsonObject

    def ReconocimientoEmociones(self,rutaImagen1):
        button = self.html.find_element_by_xpath('//*[@id="demo"]/div[3]/div/div/ol/li[3]/button')
        button.click()
        self.driver.implicitly_wait(10)
        imgInicial = self.html.find_element_by_xpath("//*[@id='emotion-results']/div/div[1]/div[1]/div/div/img")\
            .get_attribute("src")

        botonImagen1 = self.html.find_element_by_xpath(
            "//*[@id='emotion-results']/div/div[1]/div[2]/div/ul/li[3]/input")
        botonImagen1.send_keys(os.getcwd() + "/" + rutaImagen1)
        self.driver.implicitly_wait(10)
        time.sleep(5)

        imgFinal = imgInicial
        print("Esperando respuesta .........")
        contador = 0
        time.sleep(5)
        while imgInicial == imgFinal:
            if contador == 10:
                texto = self.html.find_element_by_xpath(
                    '//*[@id="emotion-results"]/div/div[2]/div/pre/code/span[11]')
                texto = texto.text
                jsonObject = json.loads(texto)
                break
            imgFinal = \
            self.html.find_element_by_xpath("//*[@id='emotion-results']/div/div[1]/div[1]/div/div/img").\
                get_attribute("src")
            time.sleep(1)
            contador = contador + 1
        else:
            texto = self.html.find_element_by_xpath(
                '//*[@id="emotion-results"]/div/div[2]/div/pre/code/span[11]')
            texto = texto.text
            jsonObject = json.loads(texto)

        return jsonObject


    def Close(self):
        self.driver.close()

if __name__ == '__main__':
    reconocimiento = Reconocimiento()
    reconocimiento.Configuracion()
    reconocimiento.Iniciar()
    #texto = reconocimiento.ReconocerRostro("Imagenes/sam.jpeg")
    texto = reconocimiento.ComprobaciónFacial("Imagenes/sca.jpg","Imagenes/sca.jpg")
    #texto = reconocimiento.ReconocimientoEmociones("Imagenes/Ana.jpg")
    print(texto)
    reconocimiento.Close()

