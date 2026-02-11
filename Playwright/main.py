from playwright.sync_api import sync_playwright
import time

url = "http://localhost:8000"
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(url)
    print(page.title())
    time.sleep(3)
    browser.close()