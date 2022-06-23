# Например, если вы хотите использовать одну и ту же аутентификацию
# для нескольких запросов, вы можете использовать сеанс:

import requests
from getpass import getpass

# используя менеджер контента, можно убедиться, что ресурсы, применимые
# во время сессии будут свободны после использования
with requests.Session() as session:
    session.auth = ('username', getpass())

    # Instead of requests.get(), you'll use session.get()
    response = session.get('https://api.github.com/user')

# здесь можно изучить ответ
print(response.headers)
print(response.json())
