import requests

url = "https://www.shutterstock.com/_next/data/5672de8ee3a/nl/search/tafel.json?term=tafel"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
print(response)