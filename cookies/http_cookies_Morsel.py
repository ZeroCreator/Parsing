# Этот пример включает в себя два различных метода для создания
# cookie с датой истечения срока жизни. Один устанавливает
# max-age как количество секунд жизни cookie с момента создания,
# другой устанавливает параметр expires как дату и время, когда
# cookie должна быть удалена.

from http import cookies
import datetime

def show_cookie(c):
    print(c)
    for key, morsel in c.items():
        print()
        print('key =', morsel.key)
        print(' value =', morsel.value)
        print(' coded_value =', morsel.coded_value)
        for name in morsel.keys():
            if morsel[name]:
                print(' {} = {}'.format(name, morsel[name]))

c = cookies.SimpleCookie()

# Cookie со значением, которое должно быть закодировано,
# чтобы поместиться в заголовок
c['encoded_value_cookie'] = '"cookie,value;"'
c['encoded_value_cookie']['comment'] = 'Has escaped punctuation'

# А эта cookie применяется только к части сайта
c['restricted_cookie'] = 'cookie_value'
c['restricted_cookie']['path'] = '/sub/path'
c['restricted_cookie']['domain'] = 'PyMOTW'
c['restricted_cookie']['secure'] = True

# Эта cookie истекает через 5 минут
c['with_max_age'] = 'expires in 5 minutes'
c['with_max_age']['max-age'] = 300  # seconds

# Cookie истекает в указанное время
c['expires_at_time'] = 'cookie_value'
time_to_live = datetime.timedelta(hours=1)
expires = (datetime.datetime(2022, 8, 14, 18, 30, 14) +
           time_to_live)

# Формат: Wdy, DD-Mon-YY HH:MM:SS GMT
expires_at_time = expires.strftime('%a, %d %b %Y %H:%M:%S')
c['expires_at_time']['expires'] = expires_at_time

show_cookie(c)


# python3 http_cookies_Morsel.py
# Set-Cookie: encoded_value_cookie="\"cookie\054value\073\""; Comment="Has escaped punctuation"
# Set-Cookie: expires_at_time=cookie_value; expires=Sat, 14 Feb 2009 19:30:14
# Set-Cookie: restricted_cookie=cookie_value; Domain=PyMOTW; Path=/sub/path; Secure
# Set-Cookie: with_max_age="expires in 5 minutes"; Max-Age=300
#
# key = encoded_value_cookie
#  value = "cookie,value;"
#  coded_value = "\"cookie\054value\073\""
#  comment = Has escaped punctuation
#
# key = restricted_cookie
#  value = cookie_value
#  coded_value = cookie_value
#  path = /sub/path
#  domain = PyMOTW
#  secure = True
#
# key = with_max_age
#  value = expires in 5 minutes
#  coded_value = "expires in 5 minutes"
#  max-age = 300
#
# key = expires_at_time
#  value = cookie_value
#  coded_value = cookie_value
#  expires = Sat, 14 Feb 2009 19:30:14


# Оба объекта Cookie и Morsel ведут себя как словари.
# Morsel отвечает за фиксированный набор значений:
# expires, path, comment, domain, max-age, secure, version.

