# В зависимости от веб-сервера и фреймворка, cookie
# доступы либо прямо из заголовка, либо из значения
# HTTP_COOKIE.
# Чтобы их раскодировать, передайте нужную часть
# cтроки в SimpleCookie, либо используйте метод load().

from http import cookies

HTTP_COOKIE = '; '.join([
    r'integer=5',
    r'with_quotes="He said, \"Hello, World!\""',
])

print('From constructor:')
c = cookies.SimpleCookie(HTTP_COOKIE)
print(c)

print()
print('From load():')
c = cookies.SimpleCookie()
c.load(HTTP_COOKIE)
print(c)

# python3 http_cookies_parse.py
# From constructor:
# Set-Cookie: integer=5
# Set-Cookie: with_quotes="He said, \"Hello, World!\""
#
# From load():
# Set-Cookie: integer=5
# Set-Cookie: with_quotes="He said, \"Hello, World!\""