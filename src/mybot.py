#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# teste
email = input('Digite o seu e-mail ou telefone: ')
password = input('Digite a sua senha: ')

driver = webdriver.Firefox()
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

# busca os elementos e coloca os valores
element_email = driver.find_element(By.XPATH, '//*[@id="username"]')
element_email.send_keys(email)

element_password = driver.find_element(By.XPATH, '//*[@id="password"]')
element_password.send_keys(password)

# envia ao servidor linkedIn os elementos acima!
element_submit = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[3]/button')
element_submit.click()
