import requests
from properties import urlPostCon
import json
def get_book_info(url):
    response = requests.get(url, params={'AuthorName': 'Rahul Shetty'})
    json_response = response.json()
    assert response.status_code == 200

    print(json_response[0]['isbn'])
    assert json_response[0]['isbn'] == 'A1b'

    print(response.headers)
    assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

    actualBook = None
    for book in json_response:
        if book['isbn'] == 'bnid34':
            actualBook = book
            print(actualBook)
            break

    expectedBook = {
        'book_name': 'Devops',
        'isbn': 'bnid34',
        'aisle': '99'
    }

    assert actualBook == expectedBook

    return actualBook

book_info = get_book_info(urlPostCon)
