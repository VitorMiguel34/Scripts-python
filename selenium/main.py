from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from typing import Any

def main():
    browser= webdriver.Chrome()
    browser.get("http://localhost:8000")

    def enviar_input_por_id(id_input: str, valor: Any) -> None:
        input = browser.find_element(By.ID, id_input)
        input.send_keys(valor)

    def clicar_em_botao_por_id(id_botao: str) -> None:
        botao = browser.find_element(By.ID, id_botao)
        botao.click()

    def buscar_texto_por_id(id_elemento: str) -> str:
        elemento = browser.find_element(By.ID, id_elemento)
        return elemento.text

    valores = {
        "inputNome": "Joao",
        "inputIdade": 16
    }

    for id,valor in valores.items():
        enviar_input_por_id(id,valor)

    clicar_em_botao_por_id("enviarDados")

    texto = buscar_texto_por_id("resultadoLogin")
    print(texto)

    if texto == "Sucesso":
        print("Login efetuado com sucesso")
    else:
        print("Falha no login")

    browser.save_screenshot("site.png")
    browser.quit()

if __name__ == "__main__":
    main()