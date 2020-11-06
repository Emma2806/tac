import requests

url = "https://quotes21.p.rapidapi.com/quote"

headers = {
    'x-rapidapi-key': "d1a20e803cmshb5f458e35acf9cdp17824cjsn0e346269462c",
    'x-rapidapi-host': "quotes21.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)