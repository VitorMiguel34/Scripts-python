import requests
from bs4 import BeautifulSoup

url = "http://localhost:8000/"
response = requests.get(url)
html = response.text
parsed_html = BeautifulSoup(html, "html.parser", from_encoding="utf-8")

print(parsed_html)
print(parsed_html.title.text)
