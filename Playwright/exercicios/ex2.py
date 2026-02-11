from playwright.sync_api import sync_playwright

url = "https://the-internet.herokuapp.com/login"

def logar(nome:str,senha:str) -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)

        page.fill("#username",nome)
        page.fill("#password",senha)
        page.click("button[type='submit']")
        
        resultado = page.locator("#flash").inner_text()
        print(resultado)
        browser.close()

logar("Victor","12")
logar("tomsmith","SuperSecretPassword!")
