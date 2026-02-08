from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://localhost:8000")

def teste_titulo():
    titulo = browser.find_element(By.TAG_NAME,"h1").text
    assert titulo == "Bem-vindo ao site"
