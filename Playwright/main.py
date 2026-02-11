from playwright.sync_api import sync_playwright
import time

url = "http://localhost:8000"
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(url)
    page.fill("#inputNome","Victor")
    page.fill("#inputIdade", "16")
    page.click("#enviarDados")

    resultado_login = page.locator("#resultadoLogin").inner_text()
    if resultado_login == "Sucesso":
        print("login realizado com sucesso!")
    else:
        print("Falha ao logar")

    time.sleep(3)
    browser.close()