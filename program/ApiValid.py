import requests
from program.config.properties import urlPostCon


class BookInfoRetriever:
    def __init__(self, url):
        self.url = url

    def fetch_book_info(self):
        response = requests.get(self.url, params={'AuthorName': 'Rahul Shetty'})
        json_response = response.json()
        assert response.status_code == 200

        print(json_response[0]['isbn'])
        assert json_response[0]['isbn'] == 'A1b'

        print(response.headers)
        assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

        actual_book = None

        def change_header(actual, new):
            nonlocal actual_book
            for book in json_response:
                if book[actual] == new:
                    actual_book = book
                    print(actual_book)
                    break

        change_header('isbn', 'bnid34')

        expected_book = {
            'book_name': 'Devops',
            'isbn': 'bnid34',
            'aisle': '99'
        }

        assert actual_book == expected_book

        return actual_book


book_retriever = BookInfoRetriever(urlPostCon)
book_info = book_retriever.fetch_book_info()
