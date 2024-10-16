import requests


url_template = 'https://wttr.in/{}?MnqT'
headers = {
    'User-Agent': 'curl',
    'Accept-Language': 'ru-Ru'
}

url_svo = url_template.format('/svo')

response_svo = requests.get(url_svo, headers=headers)
response_svo.raise_for_status()

print(response_svo.text)

url_london = url_template.format('/London')

response_london = requests.get(url_london, headers=headers)
response_london.raise_for_status()

print(response_london.text)

url_cherepovets = url_template.format("Череповец")

response_cherepovets = requests.get(url_cherepovets, headers=headers)
response_cherepovets.raise_for_status()

print(response_cherepovets.text)
