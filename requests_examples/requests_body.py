import requests

requests.post('https://httpbin.org/post', data={'key':'value'})
# <Response [200]>

requests.post('https://httpbin.org/post', data=[('key', 'value')])
# <Response [200]>

response = requests.post('https://httpbin.org/post', json={'key':'value'})
json_response = response.json()
print(json_response['data'])
# {"key": "value"}
print(json_response['headers']['Content-Type'])
# application/json