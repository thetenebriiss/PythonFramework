import requests
from program.config.properties import *

def perform_cookie_operations(urlCookSa, urlCookfi):
    cookie = {'visit-month': 'February'}
    response = requests.get(urlCookSa, allow_redirects=False, cookies=cookie, timeout=1)

    assert response.status_code == 301

    session = requests.session()
    session.cookies.update({'visit-month': 'February'})

    response = session.get(urlCookfi, cookies={'visit-year': '2022'})
    print(response.text)

perform_cookie_operations(urlCookSa, urlCookfi)
