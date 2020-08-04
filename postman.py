import requests

url = "https://deckofcardsapi.com/api/deck/k21y8s3uqkjo/"

payload = {}
headers = {
  'Cookie': '__cfduid=dece8cd736addebabec7d021d297c6ba91596189894'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))