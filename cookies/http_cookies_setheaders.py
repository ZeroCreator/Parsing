from http import cookies

c = cookies.SimpleCookie()
c['mycookie'] = 'cookie_value'
print(c)

# python3 http_cookies_setheaders.py
# Set-Cookie: mycookie=cookie_value