# Кроме использования заголовка Set-Cookie, серверы
# поставляют JavaScript, который добавляет cookie
# клиенту. SimpleCookie и Morsel генерируют J
# avaScript при использовании метода js_output().

from http import cookies
import textwrap

c = cookies.SimpleCookie()
c['mycookie'] = 'cookie_value'
c['another_cookie'] = 'second value'
js_text = c.js_output()
print(textwrap.dedent(js_text).lstrip())

# Результатом является готовый тег script
# для задания нужных значений cookie.

# python3 http_cookies_js_output.py

# <script type="text/javascript">
# <!-- begin hiding
# document.cookie = "another_cookie=\"second value\"";
# // end hiding -->
# </script>
#
# <script type="text/javascript">
# <!-- begin hiding
# document.cookie = "mycookie=cookie_value";
# // end hiding -->
# </script>