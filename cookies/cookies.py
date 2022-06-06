import requests

cookie = {'session': '17ab96bd8ffbe8ca58a78657a918558'}

r = requests.post('http://ya.ru', cookies=cookie)