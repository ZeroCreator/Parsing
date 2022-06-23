# При помощи метода prettify() можно добиться того, чтобы HTML-код выглядел аккуратнее.

from bs4 import BeautifulSoup
import requests as req

resp = req.get("http://www.something.com")

soup = BeautifulSoup(resp.text, 'lxml')

print(soup.prettify())


# <html>
#  <head>
#   <title>
#    Something.
#   </title>
#  </head>
#  <body>
#   Something.
#  </body>
# </html>