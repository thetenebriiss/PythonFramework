import requests
from payLoad import *
from program.config.properties import *
from program.config.resources import *

class BookOperationManager:
    def __init__(self, endpoint_url):
        self.endpoint_url = endpoint_url
        self.headers = {"Content-Type": "application/json"}

    def add_book(self, title, price):
        url = self.endpoint_url + ApiResources.addBook
        response = requests.post(url, json=create_book_payload(title, price), headers=self.headers)
        response_json = response.json()

        print(response_json["Msg"])
        book_id = response_json['ID']
        assert response_json["Msg"] == "successfully added"

        return book_id

    def delete_book(self, book_id):
        url = self.endpoint_url + ApiResources.deleteBook
        response = requests.post(url, json={"ID": book_id}, headers=self.headers)

        assert response.status_code == 200
        res_json = response.json()

        print(res_json["msg"])
        assert res_json["msg"] == "book is successfully deleted"

if __name__ == "__main__":
    manager = BookOperationManager(endpointUrl)

    book_id = manager.add_book("fAfsf", 1234)
    manager.delete_book(book_id)
