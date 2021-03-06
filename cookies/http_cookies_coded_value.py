# Morsel.value всегда является закодированным значением cookie,
# в то время как Morsel.coded_value всегда является представлением,
# которое используется для передачи значения клиенту. Оба значения
# всегда являются строками. Значения, которые не являются строками,
# будут автоматически преобразованы в нужный тип.

from http import cookies

c = cookies.SimpleCookie()
c['integer'] = 5
c['with_quotes'] = 'He said, "Hello, World!"'

for name in ['integer', 'with_quotes']:
    print(c[name].key)
    print('  {}'.format(c[name]))
    print('  value={!r}'.format(c[name].value))
    print('  coded_value={!r}'.format(c[name].coded_value))
    print()

# python3 http_cookies_coded_value.py
# integer
#   Set-Cookie: integer=5
#   value='5'
#   coded_value='5'
#
# with_quotes
#   Set-Cookie: with_quotes="He said\054 \"Hello\054 World!\""
#   value='He said, "Hello, World!"'
#   coded_value='"He said\\054 \\"Hello\\054 World!\\""'

