import requests
from program.config.properties import *

class CookieManager:
    def __init__(self, url):
        self.url = url
        self.session = requests.session()

    def set_cookie(self, name, value):
        self.session.cookies.update({name: value})

    def get_request(self):
        response = self.session.get(self.url)
        return response

if __name__ == "__main__":
    cookie_manager = CookieManager(urlCookSa)

    cookie_manager.set_cookie('visit-month', 'February')
    response = cookie_manager.get_request()

    assert response.status_code == 200

    cookie_manager.set_cookie('visit-year', '2022')
    response = cookie_manager.get_request()

    print(response.text)
