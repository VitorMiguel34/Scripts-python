from playwright.sync_api import sync_playwright
import time

url = "https://the-internet.herokuapp.com/upload"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)

    page.locator("#file-upload").set_input_files("ex4.txt")
    page.locator("#file-submit").click()
    time.sleep(5)
    browser.close()