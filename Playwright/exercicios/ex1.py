from playwright.sync_api import sync_playwright
import time

url = "https://duckduckgo.com"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)

    campo_pesquisar = page.locator("input[name='q']")
    campo_pesquisar.fill("playwright python")
    campo_pesquisar.press("Enter")
    time.sleep(2)

    links = page.locator("a[target='_self']")
    links.nth(0).click()
    time.sleep(2)

    texto_pagina = page.locator("main").inner_text()
    titulo = page.locator("h1").inner_text()
    topicos = page.locator("h2")
    textos_topicos = list()
    for i in range(topicos.count()):
        textos_topicos.append(topicos.nth(i).inner_text())

    print(f"Titulo: {titulo}")
    for topico in textos_topicos:
        print(topico)
        
    browser.close()
