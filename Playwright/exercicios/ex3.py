from playwright.sync_api import sync_playwright

url = "https://the-internet.herokuapp.com/dropdown"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)

    page.locator("#dropdown").select_option("1")
    value = page.locator("#dropdown").input_value()
    if value == "1":
        print("Opção 1 foi selecionada")
    else:
        print("Opção 1 não foi selecionada")
    
    browser.close()