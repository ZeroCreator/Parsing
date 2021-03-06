import requests

city = input('City?')
api_url = "http://api.openweathermap.org/data/2.5/weather"

params = {
    'q': city, #'Saint Petersburg',
    'appid': '11c0d3dc6093f7442898ee49d2430d20',
    'units': 'metric'
}

res = requests.get(api_url, params=params)
print(res.status_code)
print(res.headers["Content-Type"])
print(res.json()) # return json.loads(res.text)L
data = res.json()
template = 'Current temperature in {} is {}'
print(template.format (city, data['main']['temp']))
