import requests
from properties import *

cookie = {'visit-month':'February'}
response = requests.get(urlCookSa,allow_redirects=False,cookies=cookie,timeout=1)

assert response.status_code == 301

se = requests.session()
se.cookies.update({'visit-month':'February'})

res = se.get(urlCookfi,cookies={'visit-year':'2022'})
print(res.text)

